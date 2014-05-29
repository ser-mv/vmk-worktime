using System;
using System.Net;
using System.Collections.Specialized;
using System.Text;

namespace ClientCS
{
    public class DataTransfer
    {
        private string urlString;

        public DataTransfer(string urlString)
        {
            this.urlString = urlString;      
        }

        public string Send(NameValueCollection DataTransfNameCol)
        {
            WebClient myWebClient = new WebClient();

            // Create a new NameValueCollection instance to hold some custom parameters to be posted to the URL.
            //NameValueCollection myNameValueCollection = new NameValueCollection();

            // Add necessary parameter/value pairs to the name/value container.
            //string id = null, pass = null, workTime = null;

            //myNameValueCollection.Add("employee_id", id);
            //myNameValueCollection.Add("password", pass);
            //myNameValueCollection.Add("working_seconds", workTime);

            //string urlString = "http://kekccmakom.pythonanywhere.com/add_working_seconds";

            try
            {
                byte[] responseArray = myWebClient.UploadValues(urlString, DataTransfNameCol);
                string responseString = Encoding.ASCII.GetString(responseArray);
                return responseString;
            }
            catch
            {
                return "Error (Server Unavailable)";                
            }
            

            
        }

    }
}
