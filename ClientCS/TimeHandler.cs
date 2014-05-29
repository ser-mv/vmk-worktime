using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Timers;
using System.Collections.Specialized;
using System.Runtime.InteropServices;
using System.Diagnostics;

using UserHook;

namespace ClientCS
{
    

    class TimeHandler
    {
        #region Import

            [DllImport("user32.dll", CharSet = CharSet.Auto, ExactSpelling = true)]
            public static extern IntPtr GetForegroundWindow();

            [DllImport("user32", CharSet = CharSet.Auto, SetLastError = true)]
            public static extern int GetWindowText(IntPtr hWnd, [Out, MarshalAs(UnmanagedType.LPTStr)] StringBuilder lpString, int nMaxCount);

            [DllImport("user32.dll", SetLastError = true)]
            static extern int GetWindowThreadProcessId(IntPtr hWnd, out int lpdwProcessId);

        #endregion

        private DateTime lastTimeEvent;
        public int curWorkTime;
        private TimeSpan timedif;
        private int timeOutSeconds;
        private string url;
        private config cfg;
        private UserActivityHook actHook;

        public TimeHandler(config cfg)
        {
            lastTimeEvent = DateTime.Now;
            curWorkTime = 0;
            this.cfg = cfg;
            this.url = cfg.url;
            this.timeOutSeconds = cfg.timeOut;
        }

        public void MouseMoved(object sender, MouseEventArgs e)
        {
            //labelMousePosition.Text = String.Format("x={0}  y={1} wheel={2}", e.X, e.Y, e.Delta);
            //if (e.Clicks > 0) LogWrite("MouseButton 	- " + e.Button.ToString());
           // lastTimeEvent = DateTime.Now;
            checkProc();
        }

        public void MyKeyDown(object sender, KeyEventArgs e)
        {
            //LogWrite("KeyDown 	- " + e.KeyData.ToString());
            //lastTimeEvent = DateTime.Now;
            checkProc();

        }

        public void MyKeyPress(object sender, KeyPressEventArgs e)
        {
            //LogWrite("KeyPress 	- " + e.KeyChar);
            //lastTimeEvent = DateTime.Now;
            checkProc();
        }

        public void MyKeyUp(object sender, KeyEventArgs e)
        {
            //LogWrite("KeyUp 		- " + e.KeyData.ToString());
            //lastTimeEvent = DateTime.Now;
            checkProc();
        }

        //private void LogWrite(string txt)
        //{
        //    richTextBox1.AppendText(txt + Environment.NewLine);
        //    richTextBox1.SelectionStart = richTextBox1.Text.Length;
        //}

        private void checkProc()
        {
            IntPtr hwin = GetForegroundWindow();

            int processID = 0;
            int threadID = GetWindowThreadProcessId(hwin, out processID);
            
            Process localById = Process.GetProcessById(processID);    

            foreach(string s in cfg.proclist)
            {
                if (localById.ProcessName.Equals(s))
                {
                    lastTimeEvent = DateTime.Now;
                }

            }

        }

        public void setHook(bool onOff)
        {

            if (onOff)
            {
                actHook = new UserActivityHook(true, true);
                actHook.OnMouseActivity += new MouseEventHandler(MouseMoved);
                actHook.KeyDown += new KeyEventHandler(MyKeyDown);
                actHook.KeyPress += new KeyPressEventHandler(MyKeyPress);
                actHook.KeyUp += new KeyEventHandler(MyKeyUp);
            }
            else
            {
                actHook.Stop();
                this.DeleteCurWorktime();
            }
        }

        public void addWorkTime(int seconds)
        {           
            if(!checkTimeout())
                curWorkTime = seconds;
        }

        private bool checkTimeout()
        {
            timedif = DateTime.Now.Subtract(lastTimeEvent);
            if (timedif.Seconds >= timeOutSeconds)
                return true;
            else return false;
        }

        public string SendWorkingTime(string ID, string pass)
        {
            NameValueCollection myNameValueCollection = new NameValueCollection();

            string workTime = (1800*curWorkTime).ToString();

            myNameValueCollection.Add("employee_id", ID);
            myNameValueCollection.Add("password", pass);
            myNameValueCollection.Add("working_seconds", workTime);

            DataTransfer d = new DataTransfer(url);
            return d.Send(myNameValueCollection);
        }
        private void DeleteCurWorktime()
        {
            this.curWorkTime = 0;
        }
    }
}
