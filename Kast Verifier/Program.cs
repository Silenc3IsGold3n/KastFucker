using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using MailKit.Net.Imap;
using MailKit.Search;
using MailKit;
using MimeKit;
using System.Text.RegularExpressions;
using System.IO;

namespace Kast_Verifier
{
    class Program
    {
		public static void Main(string[] args)
		{

			string login = "youremailaddress@gmail.com";
			string password = "youremailaddresspassword!123";
			string dateToCheckFrom = "2020-11-01"; // Date you started running KastFucker (so it knows when to check from when it checks your emails) its in YYYY-MM-DD
			using (var client = new ImapClient())
			{
				client.Connect("imap.gmail.com", 993, true);

				client.Authenticate(login, password);

				// The Inbox folder is always available on all IMAP servers...
				var inbox = client.Inbox;
				inbox.Open(FolderAccess.ReadOnly);

				Console.WriteLine("Total messages: {0}", inbox.Count);
				Console.WriteLine("Recent messages: {0}", inbox.Recent);
				var query = SearchQuery.DeliveredAfter(DateTime.Parse(dateToCheckFrom))
	.And(SearchQuery.SubjectContains("Kast"));

				string path = @"verificationcodes-new.txt";

				if (!File.Exists(path))
				{
					// Create a file to write to.
					using (StreamWriter sw = File.CreateText(path))
					{
					}
				}

				foreach (var uid in inbox.Search(query))
				{
					var message = inbox.GetMessage(uid);
					//Console.WriteLine("[match] {0}: {1}", uid, message.Subject);
					Match a = Regex.Match(message.TextBody, "\\*Hey ...");
					string accountname = a.ToString().Split(' ')[1];
					Match b = Regex.Match(message.TextBody, "\\d\\d\\d\\d\\d\\d");
					using (StreamWriter sw = File.AppendText(path))
					{
						sw.WriteLine(accountname + ":" + b.ToString());
					}
					Console.WriteLine(accountname+ ":"+b.ToString());
				}


				client.Disconnect(true);
			}
		}
	}
}
