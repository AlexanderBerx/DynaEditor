import logging
from maya import cmds


class JobManager(object):
    """
    Singleton class for creating & managing maya script jobs, when a new
    script job is created it's being stored in the instance so it
    can keep track of all the created maya script jobs
    """
    _job_list = []

    def __new__(cls):
        """
        creates a new instance of the class if none exists yet,
        returns the existing one if already exists
        :return: JobManager
        """
        logger = logging.getLogger(__name__)
        logger.debug("Creating instance of  {}".format(cls))
        if not hasattr(cls, 'instance'):
            logger.debug("using existing instance of  {}".format(cls))
            cls.instance = super(JobManager, cls).__new__(cls)
        return cls.instance

    def create_job(self, *args, **kwargs):
        """
        creates a script job with the given args & kwargs, and stores it's id
        internally returns the id of the created job
        :param args:
        :param kwargs:
        :return: str
        """
        logger = logging.getLogger(__name__)
        logger.debug("Creating new script job")
        job = cmds.scriptJob(*args, **kwargs)
        self._job_list.append(job)
        logger.debug("Creating script job: {}".format(job))
        return job

    def clean_up_jobs(self):
        """
        remove all the script jobs stored within the instance
        :return: None
        """
        logger = logging.getLogger(__name__)
        logger.debug("cleaning up script job")
        for job in self._job_list:
            cmds.scriptJob(kill=job, force=True)
            self._job_list.remove(job)
            logger.debug("Removed script job: {}".format(job))
