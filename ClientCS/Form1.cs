using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
using System.Timers;
using System.Diagnostics;

using UserHook;

namespace ClientCS
{
    public partial class Form1 : Form
    {
        //private string url;
        //private TimeHandler t;
        //private Autorization a;
        //private config cfg;
        //private System.Timers.Timer timer;
        //private int sumWorktime;

        private Controller c;

        public Form1()
        {
            InitializeComponent();

            //cfg = new config();
            //cfg.readConfig();

            //t = new TimeHandler(cfg);
            //t.timeOutMin = 10;
            c = new Controller();


        }


        private void button1_Click(object sender, EventArgs e)
        {
            label1.Text = "Status";
            //a = new Autorization(cfg.url);
            //string status = a.CheckIdPass(textBoxID.Text, textBoxPass.Text);
            //label1.Text = status;

            //status = "ok";

            string status = c.Autorization(textBoxID.Text, textBoxPass.Text);
            label1.Text = status;

            if (status != null && status.Equals("ok"))
            //if (status == "ok")
            {
                textBoxID.Enabled = false;
                textBoxPass.Enabled = false;
                button1.Enabled = false;
                button1.Visible = false;
                button2.Visible = true;
                button2.Enabled = true;

                c.StartWork();

                System.Timers.Timer timer = new System.Timers.Timer();

                //t.setHook(true);

                timer.Elapsed += new ElapsedEventHandler(TimerEvent);
                timer.Interval = 10000;
                timer.Start();

            }
            else
            {
                if (notifyIcon1.Visible)
                {
                    notifyIcon1.BalloonTipText = status;
                    notifyIcon1.ShowBalloonTip(5000);
                }
            }

        }

        private void textBoxID_Click(object sender, EventArgs e)
        {
            if(textBoxID.Text == "ID")
                textBoxID.Text = "";
            textBoxID.ForeColor = System.Drawing.Color.Black;
        }

        private void textBoxPass_Click(object sender, EventArgs e)
        {
            if (textBoxPass.Text.Equals("Password"))
                textBoxPass.Text = "";
            textBoxPass.ForeColor = System.Drawing.Color.Black;

        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            if (this.WindowState == FormWindowState.Minimized)
            {
                //this.WindowState = FormWindowState.Minimized;
                notifyIcon1.Visible = true;
                this.Hide();
                this.ShowInTaskbar = false;
            }
        }

        private void notifyIcon1_DoubleClick(object sender, EventArgs e)
        {
            this.Show();
            WindowState = FormWindowState.Normal;
            notifyIcon1.Visible = false;
            this.ShowInTaskbar = true;
        }

        public void TimerEvent(object source, ElapsedEventArgs e)
        {
            ////string s = t.addWorkTime(cfg.freq
            //t.addWorkTime(cfg.freq);

            //string status = t.SendWorkingTime(a.ID, a.pass);
            ////sumWorktime += t.curWorkTime;
            ////notifyIcon1.BalloonTipText = status + " " + t.curWorkTime.ToString();
            ////label1.Text = sumWorktime.ToString();
            ////notifyIcon1.BalloonTipText = status + " " + sumWorktime.ToString();
            ////notifyIcon1.ShowBalloonTip(5000);
            //if (status != null && !status.Equals("ok"))
            //{
            //    label1.Text = status;
            //    notifyIcon1.BalloonTipText = status;
            //    notifyIcon1.ShowBalloonTip(5000);
            //}

            ////richTextBox1.AppendText("curwt =" + t.curWorkTime.ToString() + Environment.NewLine);
            ////richTextBox1.SelectionStart = richTextBox1.Text.Length;
            ////richTextBox1.AppendText("timediff = " + t.timedif.Seconds.ToString() + Environment.NewLine);
            ////richTextBox1.SelectionStart = richTextBox1.Text.Length;

            ////richTextBox1.AppendText("wintext = " + s + Environment.NewLine);
            ////richTextBox1.SelectionStart = richTextBox1.Text.Length;
            ////t.checkProc();

            string status = c.GetStatus();

            if (status != null && !status.Equals("ok"))
            {
                label1.Text = status;
                notifyIcon1.BalloonTipText = status;
                notifyIcon1.ShowBalloonTip(5000);
            }

        }

        private void button2_Click(object sender, EventArgs e)
        {
            label1.Text = "Logged Out";

            textBoxID.Enabled = true;
            textBoxPass.Enabled = true;
            button1.Enabled = true;
            button1.Visible = true;
            button2.Visible = false;
            button2.Enabled = false;

            c.StopWork();

            //t.setHook(false);
            //a.DeleteAutorization();
            //timer.Stop();



        }

    }
}
