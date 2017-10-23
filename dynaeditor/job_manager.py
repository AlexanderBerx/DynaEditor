from maya import cmds


class JobManager(object):
    _job_list = []

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(JobManager, cls).__new__(cls)
        return cls.instance

    def create_job(self, *args, **kwargs):
        job = cmds.scriptJob(*args, **kwargs)
        print("Created job", job)
        self._job_list.append(job)

    def clean_up_jobs(self):
        for job in self._job_list:
            cmds.scriptJob(kill=job, force=True)
            self._job_list.remove(job)
            print("Removed job", job)
