using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using System.Timers;
using System.Diagnostics;

namespace ClientCS
{
    class Controller
    {
        #region FieldsOfModel
            private TimeHandler t;
            private Autorization a;
            private config cfg;
            private System.Timers.Timer timer;
        #endregion

        private string status;

        public Controller()
        {
            cfg = new config();
            cfg.readConfig();
            t = new TimeHandler(cfg);
        }

        public string GetStatus()
        {
            return status;
        }

        public string Autorization(string ID, string Pass)
        {
            a = new Autorization(cfg.url);
            status = a.CheckIdPass(ID, Pass);

            return GetStatus();
        }

        public string StartWork()
        {
            timer = new System.Timers.Timer();
            t.setHook(true);
            timer.Elapsed += new ElapsedEventHandler(TimerEvent);
            timer.Interval = cfg.freq * 1000;
            timer.Start();

            return GetStatus();
        }
        public string StopWork()
        {
            t.setHook(false);
            a.DeleteAutorization();
            timer.Stop();

            return GetStatus();
        }

        private void TimerEvent(object source, ElapsedEventArgs e)
        {
            t.addWorkTime(cfg.freq);
            status = t.SendWorkingTime(a.ID, a.pass);
        }

    }
}
