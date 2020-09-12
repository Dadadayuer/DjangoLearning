from .utf import encode as encode_utf7, decode as decode_utf7
from .message import Message

class MailBox():

    def __init__(self,mail,name="INBOX"):
        self.name = name
        self.date_format = "%d-%b-%y"
        self.messages={}
        self.mail = mail

    def external_name(self):
        if 'external_name' not in vars(self):
            vars(self)['external_name']=encode_utf7(self.name)
        return vars(self)['external_name']

    def external_name(self,value):
        if 'external_name' in vars(self):
            del vars(self)['external_name']
        self.name = encode_utf7(value)


    def Mail(self,prefetch = False, **kwargs):
        search = ['ALL']

        kwargs.get('read') and search.append('SEEN')
        kwargs.get('unread') and search.append('UNSEEN')

        kwargs.get('starred') and search.append('FLAGGED')
        kwargs.get('unstarred') and search.append('UNFLAGGED')

        kwargs.get('deleted') and search.append('DELETED')
        kwargs.get('undeleted') and search.append('UNDELETED')

        kwargs.get('draft') and search.append('DRAFT')
        kwargs.get('undraft') and search.append('UNDRAFT')

        kwargs.get('before') and search.extend(['BEFORE',kwargs.get('before').strftime(self.date_format)])
        kwargs.get('after') and search.extend(['SINCE',kwargs.get('after').strftime(self.date_format)])
        kwargs.get('on') and search.extend(['ON',kwargs.get('on').strftime(self.date_format)])

        kwargs.get('header') and search.extend(['HEADER',kwargs.get('header')[0],kwargs.get('header')[1]])

        kwargs.get('sender') and search.extend(['FROM',kwargs.get('sender')])
        kwargs.get('fr') and search.extend(['FROM',kwargs.get('fr')])
        kwargs.get('to') and search.extend(['TO',kwargs.get('to')])
        kwargs.get('cc') and search.extend(['CC',kwargs.get('cc')])

        kwargs.get('subject') and search.extend(['SUBJECT', kwargs.get('subject')])
        kwargs.get('body') and search.extend(['BODY', kwargs.get('body')])

        kwargs.get('label') and search.extend(['X-GM-LABELS', kwargs.get('label')])
        kwargs.get('attachment') and search.extend(['HAS', 'attachment'])

        kwargs.get('query') and search.extend([kwargs.get('query')])

        emails = []
        response,data =self.mail.imap.uid('SEARCH',*search)
        if response == 'OK':
            uids = filter(None, data[0].split(' '))

            for uid in uids:
                if not self.messages.get(uid):
                    self.messages[uid] =Message(self,uid)
                emails.append(self.messages[uid])

            if prefetch and emails:
                messages_dict= {}
                for email in emails:
                    messages_dict[email.uid]= email
                self.messages.update(self.mail.fetch_multiple_messages(messages_dict))

        return emails