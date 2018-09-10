# -*- encoding:UTF-8 -*-

def Get_Python_Job(JobName=None):
    if JobName == "BSP_NightlyBuild":
        import BSP_NightlyBuild
        return BSP_NightlyBuild
    else:
        import Default
        return Default
