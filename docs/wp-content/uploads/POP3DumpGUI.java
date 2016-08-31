/*
 * This source code is
 * Copyright 2004 Christopher Swenson
 * (christopher-swenson@utulsa.edu)
 *
 * Since, in some far off future, I may include this code
 * or some derivative in a commercial product, any copying
 * or distributing of this code requires written permission
 * of the author.
 *
 * version 2.0
 */

import java.io.*;
import java.net.*;
import java.util.Vector;
import java.util.StringTokenizer;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import static javax.swing.JOptionPane.showInputDialog;
import static javax.swing.JOptionPane.showMessageDialog;

public class POP3DumpGUI extends JFrame
{
	String server = null;
	String user = null;
	int port = 110;
	String password = null;
	String outFile = null;
	boolean verbose = false;
	int numToSave = -1;
	boolean displayStatsOnly = false;
	boolean delete = false;

	POP3DumpGUI()
	{
		super("POP3 Dump");

		//setSize(400, 300);

		//setVisible(true);
	}

	void parseArgs(String[] args)
	{
		try
		{
			for (int i = 0; i < args.length; i++)
			{
				if (args[i].equals("-s"))
				{
					server = args[++i];
				}
				else if (args[i].equals("-u"))
				{
					user = args[++i];
				}
				else if (args[i].equals("-p"))
				{
					port = Integer.parseInt(args[++i]);
				}
				else if (args[i].equals("-P"))
				{
					password = args[++i];
				}
				else if (args[i].equals("-o"))
				{
					outFile = args[++i];
				}
				else if (args[i].equals("-v"))
				{
					verbose = true;
				}
				else if (args[i].equals("-d"))
				{
					numToSave = Integer.parseInt(args[++i]);
				}
				else if (args[i].equals("--delete"))
				{
					delete = true;
				}
				else if (args[i].equals("--stats"))
				{
					displayStatsOnly = true;
				}
				else if (args[i].equals("--help"))
				{
					System.err.println("Options available:");
					System.err.println("\t-o outfile   Sends dump of all emails from POP3 to a");
					System.err.println("\t             file (Default is standard out)");
					System.err.println("\t-s server    POP3 server to connect to");
					System.err.println("\t-u user      User name to connect to the server with");
					System.err.println("\t-p port      Port to connect to the POP3 server with");
					System.err.println("\t             (Default is 110)");
					System.err.println("\t-P password  Password to connect to the server with");
					System.err.println("\t-v           Be more verbose");
					System.err.println("\t--stats      Display stats only");
					System.err.println("\t--delete     Delete from server after downloading");
					System.exit(0);
				}
				else
				{
					throw new Exception();
				}
			}
		}
		catch (Exception e)
		{
			System.err.println("Problem with arguments around.");
			System.exit(1);
		}

	}

	public static void main(String[] args)
	{
		POP3DumpGUI program = new POP3DumpGUI();
		program.parseArgs(args);
		program.run();
	}

	void run()
	{
		try
		{
			if (server == null)
				server = showInputDialog(this, "Server name:").toString();

			if (user == null)
				user = showInputDialog(this, "User name:").toString();

			if (password == null)
				password = showInputDialog(this, "Password:").toString();

			if (outFile == null)
				outFile = showInputDialog(this, "Output file name:").toString();

			PrintStream out = new PrintStream(new FileOutputStream(outFile));

			Socket pop3 = new Socket(server, port);

			BufferedWriter pop3out = new BufferedWriter(new OutputStreamWriter(pop3.getOutputStream(), "UTF-8"));

			BufferedReader pop3in = new BufferedReader(new InputStreamReader(pop3.getInputStream()));

			pop3in.readLine();
			boolean authenticated = false;
			String crlf = "\r\n";
			boolean first = true;

			while (!authenticated)
			{
				if (first)
				{
					first = false;
				}
				else
				{
					System.err.println("Authorization error... trying again in 10 seconds...");
					try
					{
						Thread.sleep(10000);
					}
					catch (InterruptedException ie)
					{
					}
				}
				pop3out.write("USER " + user + crlf);
				pop3out.flush();
				String input = pop3in.readLine();
				if (!input.startsWith("+OK"))
					continue;

				pop3out.write("PASS " + password + crlf);
				pop3out.flush();
				input = pop3in.readLine();

				if (!input.startsWith("+OK"))
					continue;

				authenticated = true;
			}

			while (authenticated)
			{
				pop3out.write("LIST" + crlf);
				pop3out.flush();
				String input = pop3in.readLine();
				if (!input.startsWith("+OK"))
					break;

				int count = -1;
				long totalSize = 0;
				Vector<Integer> retrs = new Vector<Integer>();
				Vector<Long> sizes = new Vector<Long>();

				while (!input.equals("."))
				{
					count++;
					input = pop3in.readLine();

					if (!input.equals("."))
					{
						StringTokenizer st = new StringTokenizer(input);
						retrs.add(Integer.parseInt(st.nextToken()));
						long size = Long.parseLong(st.nextToken());
						sizes.add(size);
						totalSize += size;
					}
				}

				if (displayStatsOnly || verbose)
				{
					System.err.println("Files Found: " + retrs.size() + ".  Size: " + totalSize + " bytes = " + (totalSize >> 10) + " KB = " + (totalSize >> 20) + " MB");
					if (!displayStatsOnly) System.err.println("Retrieving...");
				}
				if (!displayStatsOnly)
				{
					long currSize = 0;

					ProgressMonitor pm = new ProgressMonitor(this, "Dumping data off...", "0M of " + (totalSize >> 20) + "M", 0, (int) (totalSize >> 10));

					for (int i = 0; !pm.isCanceled() && i < retrs.size(); i++)
					{
						int retr = retrs.get(i).intValue();
						pop3out.write("RETR " + retr + crlf);
						pop3out.flush();

						input = pop3in.readLine();
						if (input.startsWith("+OK"))
						while (!input.equals("."))
						{
							input = pop3in.readLine();
							out.println(input);
						}

						currSize += sizes.get(i).longValue();
						pm.setProgress((int) (currSize >> 10));
						pm.setNote((currSize >> 20) + "M of " + (totalSize >> 20) + "M");
						if (delete)
							if (retrs.size() - i > numToSave)
							{
								pop3out.write("DELE " + retr + crlf);
								pop3out.flush();
								pop3in.readLine();
							}
					}
					break;

				}
				authenticated = false;
			}

			String input = "--";
			while (!input.startsWith("+OK"))
			{
				pop3out.write("QUIT" + crlf);
				pop3out.flush();
				input = pop3in.readLine();
			}
		}
		catch (Exception e)
		{
			System.err.println(e);
			e.printStackTrace();
			System.exit(1);
		}

		System.exit(0);
	}
}
