using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace ClientCS
{
    class config
    {
        public string url;
        public int timeOut;
        public int freq;
        //public string[] procList;
        public List<string> proclist;

        //public void readConfig()
        //{
        //    proclist = new List<string>();
        //    StreamReader file = new StreamReader("config.cfg");
        //    url = file.ReadLine();
        //    timeOut = Convert.ToInt32(file.ReadLine());
        //    freq = Convert.ToInt32(file.ReadLine());

        //    string str = null;
        //    while ((str = file.ReadLine()) != null)
        //    {
        //        proclist.Add(str);
        //    }

        //}

        public void readConfig()
        {
            proclist = new List<string>();
            StreamReader file = new StreamReader("config.cfg");

            string str = null;
            while ((str = file.ReadLine()) != null)
            {
                if (str.Contains("<url>"))
                {
                    url = file.ReadLine();
                }
                if (str.Contains("<TimeOut>"))
                {
                    timeOut = Convert.ToInt32(file.ReadLine());
                }
                if (str.Contains("<Frequency>"))
                {
                    freq = Convert.ToInt32(file.ReadLine());
                }
                if (str.Contains("<List of processes>"))
                {
                    while ((str = file.ReadLine()) != null)
                    {
                        proclist.Add(str);
                    }
                }

            }

            //url = file.ReadLine();
            //timeOut = Convert.ToInt32(file.ReadLine());
            //freq = Convert.ToInt32(file.ReadLine());

            //string str = null;
            //while ((str = file.ReadLine()) != null)
            //{
            //    proclist.Add(str);
            //}

        }

    }
}
