# -*- encoding:UTF-8 -*-

def Get_Python_Job(JobName=None):
    if JobName == "BSP_NightlyBuild":
        import BSP_NightlyBuild
        return BSP_NightlyBuild
    elif JobName == "BSP_TiggerBuild":
        import BSP_TiggerBuild
        return BSP_TiggerBuild
    else:
        import Default
        return Default
