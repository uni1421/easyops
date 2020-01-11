from __future__ import absolute_import, unicode_literals

from celery import shared_task
from easyops.celery import app
import logging
import traceback
from django.core.mail import send_mail, send_mass_mail, EmailMultiAlternatives, EmailMessage
from easyops.settings import EMAIL_HOST_USER, MEDIA_URL, MEDIA_ROOT
import string
import random
import re


logger = logging.getLogger(__name__)


def get_random_code(num=6):
    s = string.ascii_lowercase + string.digits

    return ''.join(random.sample(s, num))

emilpattern = re.compile(r".*@.*")
phonepattern = re.compile(r"[0-9]{11}")


@app.task()
def send_msg_mail(user_email, email_body, email_title=''):
    try:
        send_status = send_mail(email_title, email_body, EMAIL_HOST_USER, [user_email])
        logger.info('邮件发送状态：{}'.format(send_status))
    except Exception as er:
        logger.error("err: {},邮件发送失败: {}".format(er, user_email))
    return

