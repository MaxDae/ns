__author__ = 'mvasin'
import requests
import json
from BeautifulSoup import BeautifulSoup as bs
import os

server_url = "http://216.166.0.216/hs/"

class clientData(object):
    def __init__(self, username, passwd, server_url):
        self.username = username
        self.passwd = passwd
        self.url = server_url
        self.s = requests.session()
        self.login_url = self.url+"{0}".format("login.hs")
        querystring =  {"username":"{0}".format(self.username),"password":"{0}".format(self.passwd)}
        self.s.get(self.login_url, headers = {}, params = querystring)
        self.s.headers.update({"referer": self.login_url+"?username={0}".format(self.username)+"&password={0}".format(self.passwd)})

    def getClientEmployeesNames(self):
        employees = self.s.get(self.url+"{0}".format("spring/client/employee/"), headers = {})
        employees = employees.json()
        names = {}
        for uid in employees:
            if uid['visible'] == True:
                names[uid['id']] = uid['name']
        return names

    def getEmployeeSchedules(self, employee_id):
         employees = self.s.get(self.url+"{0}".format("spring/client/employee/"), headers = {})
         employees = json.loads(employees, "ascii")
         for eid in employees:
             if eid['id'] == employee_id:
                 return eid['schedules']

    def getJobsLocation(self):
        """
        : dict list
        """
        jl_map = {}
        job_location = self.s.get(self.url+"{}".format("spring/scheduling/bootstrap"), headers = {})
        job_location = job_location.json()
        #job_location = [str.encode("utf-8") for str in job_location]

        for job in job_location["jobs"]:
            jl_map.update({job["name"].encode('ascii'): [ x["name"].encode('ascii') for x in job["locationList"] if x["disabled"] != "false"]})

        return jl_map

    def get_disabled_jobs(self):
         jobs = self.s.get(self.url+"{}".format("spring/scheduling/bootstrap"), headers = {})
         jobs = jobs.json()
         disabled_jobs = [x["name"].encode('ascii') for x in jobs["jobs"] if x["disabled"] != False and x["visible"] != False]
         return disabled_jobs

    def get_jobs_payrate(self):
         jobs = self.s.get(self.url+"{}".format("spring/scheduling/bootstrap"), headers = {})
         jobs = jobs.json()
         jobs_payrate = {}
         jobs_payrate.update({x["name"].encode("ascii") : int(x["payRate"]) for x in jobs["jobs"]})
         return jobs_payrate

    def get_schedules(self):
        """
        : dictionary schedule_name : schedule_id
        """
        schedule = self.s.get(self.url+"{}".format("spring/scheduling/bootstrap"), headers = {})
        schedule = schedule.json()
        schedules = {}
        schedules.update({int(x["id"]) : x["name"].encode("ascii") for x in schedule["schedules"] if x["disabled"] == False})
        return schedules

    """
    {"id":-372479002,"ownerId":17356249,"startDate":"2016-06-01","startTime":"15:30",
     "duration":480,"jobId":1024432442,"roleId":1024432433,"locationId":-1,"house":false,"dayPartId":1024432540,"regHours":8,"ovtHours":0,"regPay":9600,"ovtPay":0,"clientId":0}
    """

    """
        "jobs": [
    {
      "id": 1024432542,
      "name": "manager",
      "type": 1,
      "disabled": false,
      "updateable": true,
      "visible": false,
      "errorCode": 0,
      "success": true,
      "defaultScheduleId": 1024432541,
      "externalRef": -1,
      "payRate": 0,
      "locationList": [
        {
          "id": -1,
          "name": "None"


    """
  
env = next(x for x in os.environ['PYTHONPATH'].split(';') if 'new_scheduler_tests' in x)
#env.index('new_scheduler_tests')
print env
if 'nt' in os.name:
    res = os.path.join(env, '\\recources')
elif "nix" in os.name:
    res = os.path.join(env, '/recources')




