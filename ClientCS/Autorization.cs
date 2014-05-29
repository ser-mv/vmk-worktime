using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Collections.Specialized;

namespace ClientCS
{
    class Autorization
    {
        private string url;
        public string ID;
        public string pass;

        public Autorization(string urlstr)
        {
            this.url = urlstr;
            
        }

        public string CheckIdPass(string ID, string pass)
        {
            this.ID = ID;
            this.pass = pass;

            NameValueCollection myNameValueCollection = new NameValueCollection();

            string workTime = "0";

            myNameValueCollection.Add("employee_id", ID);
            myNameValueCollection.Add("password", pass);
            myNameValueCollection.Add("working_seconds", workTime);

            DataTransfer d = new DataTransfer(url);
            return d.Send(myNameValueCollection);
        }

        public void DeleteAutorization()
        {
            this.ID = null;
            this.pass = null;
        }
    }
}
