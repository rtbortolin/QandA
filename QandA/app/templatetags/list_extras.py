from django.template import Library
import logging
logger = logging.getLogger(__name__)
del logging

register = Library()

@register.filter
def sort_answer(value):
    logger.error('calling')
    logger.info(__name__)
    try:
        value_list = list(value)
        value_list =  sorted(value_list, key=lambda a: a.vote_score(), reverse = True)
        #value_list =  sorted(value_list, key=lambda a: a.vote_score, reverse = True)
        for answer in value_list:
            logger.info('loop')
            logger.info(str(answer.id) + ' - ' + str(answer.vote_score()))

        return value_list
    except Exception, e:
        logger.error(e)
        return ''