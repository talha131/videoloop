def check_positive(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(
            "Positive number is required. %s is invalid" % value)
    return ivalue


def secondsToText(secs):
    days = secs//86400
    hours = (secs - days*86400)//3600
    minutes = (secs - days*86400 - hours*3600)//60
    seconds = secs - days*86400 - hours*3600 - minutes*60
    result = ("{0} day{1}, ".format(days, "s" if days != 1 else "") if days else "") + \
        ("{0} hour{1}, ".format(hours, "s" if hours != 1 else "") if hours else "") + \
        ("{0} minute{1}, ".format(minutes, "s" if minutes != 1 else "") if minutes else "") + \
        ("{0} second{1}".format(
            seconds, "s" if seconds != 1 else "") if seconds else "")
    return result
