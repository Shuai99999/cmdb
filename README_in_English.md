This is a Django project I wrote to quickly handle some cumbersome tasks in my daily work.

Initially, I wanted it to take on the responsibilities of CMDB. You can see that there are some places to enter system information and server information. There is a MySQL database in the background for data storage.

Later, because I was too busy to maintain a real CMDB myself, it evolved into only providing these functions in the last tab "Function" page.

Because I am the company's DBA, many functions are related to the database. These functions are briefly described as follows:

WMS national derivative and WMS center export, these two are used to export data from the WMS app database. Because the app has a design of sharding-table, after the user submits a derivative application on ITSM, the call center supporter can help the user to export by self-service, without actually asking for my help export, which is a slacking function to me;

Import temporary data, used for the call center supporter to temporarily process a batch of data, the corresponding data ID to be processed can be entered into a temporary table, so that the where clause “where (select id from tmp_data)” can be used for subquery SQL to export data or change data. Otherwise, the normal SQL condition will fail if the subquery “in” exceeds 1000, which is also a DBA slacking off function;

MyCAT user management, used to change the user addition, deletion and authorization operation of the MyCAT database middleware from modifying its xml to a graphical interface, but this function was not actually used in practice;
f
Upload/download files, this function is not actually used too;

Re-execute data change processes. Sometimes the data change process submitted by the call center supporter will fail for some reason. This function is used to re-execute the data change processes in the ITSM process they submitted themselves, and can feed back the SQL error information of the failed execution on the page. After seeing it, they, the supporters, can submit it again according to the error information. It is also a DBA slacking off function, otherwise the supports may drive me mad 100 times per day;

Set export data tasks. Some of the app users propose to export certain data from the database at a fixed time periodically. This function is used to directly set the export data task. After entering the crontab format, database address, and SQL, the job can be set up in the background. So the supporters never need to find a DBA to handle it manually. The ultra slacking off function!


