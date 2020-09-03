import imaplib
from enum import Enum



class Mail():


    def __init__(self):
        self.username = None
        self.password =None
        self.access_token = None

        self.imap = None
        self.smtp = None
        self.logged_in = False
        self.mailboxes={}
        self.current_mailbox = None
        self.host=None
        self.port=None


    def connect(self,host,port):
        self.host =host
        self.port =port
        self.imap =imaplib.IMAP4_SSL(host,port)
        return self.imap


    def fetch_mailboxs(self):
        response, mailbox_list =self.imap.list()
        if response == 'OK':
            for mailbox in mailbox_list:
                pass



    def login(self,username,password):
        self.username = username
        self.password = password

        if not self.imap:
            self.connect(self.host,self.port)
        imap_login =self.imap.login(username,password)
        self.logged_in = (imap_login and imap_login[0] == 'OK')
        return self.logged_in







class Mail_host(Enum):
    host_imap_QQ = 'imap.qq.com'
    host_smtp_QQ = 'smtp.qq.com'
    host_pop_QQ = 'pop.qq.com'

    host_imap_163 = 'imap.163.com'
    host_smtp_163 = 'smtp.163.com'
    host_pop3_163 = 'pop.163.com'


class Mail_port(Enum):
    port_imap_QQ = 993
    port_smtp_QQ_1 = 465
    port_smtp_QQ_2 = 587
    port_pop_QQ = 995

    port_imap_163 = 993
    port_smtp_163_1 = 465
    port_smtp_163_2 = 994
    port_pop3_163 = 995


