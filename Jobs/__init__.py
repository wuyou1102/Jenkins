# -*- encoding:UTF-8 -*-

def Get_Python_Job(JobName=''):
    if JobName == "C2_DailyBuild":
        import C2
        return C2
    elif JobName == "BSP_TiggerBuild":
        import BSP_TiggerBuild
        return BSP_TiggerBuild
    elif JobName.startswith('B29A') or JobName.startswith('B29B'):
        import B2
        return B2
    elif JobName == "C2_CleanupSourceCode":
        import C2
        return C2
    elif JobName == "C2_Release_WeeklyBuild":
        import C2
        return C2
    else:
        from Default import Job
        return Job
