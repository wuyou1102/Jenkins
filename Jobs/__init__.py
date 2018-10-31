# -*- encoding:UTF-8 -*-

def Get_Python_Job(JobName=None):
    if JobName == "BSP_NightlyBuild":
        from C2 import Job
        return Job
    elif JobName == "BSP_TiggerBuild":
        import BSP_TiggerBuild
        return BSP_TiggerBuild
    elif JobName == "B2_DailyBuild":
        from B2 import Job
        return Job
    elif JobName == "C2_CleanupSourceCode":
        from C2 import Job
        return Job
    else:
        from Default import Job
        return Job
