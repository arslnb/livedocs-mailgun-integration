from functions import datapoints


dispatch = {
    'GET_ACCEPTED': datapoints.get_stats,
    'GET_DELIVERED': datapoints.get_stats,
    'GET_FAILED': datapoints.get_stats,
    'GET_OPENED': datapoints.get_stats,
    'GET_CLICKED': datapoints.get_stats,
    'GET_UNSUBSCRIBED': datapoints.get_stats,
    'GET_COMPLAINED': datapoints.get_stats,
    'GET_STORED': datapoints.get_stats
}
