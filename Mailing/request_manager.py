from sql import execute
class RequestManager:
    @staticmethod
    def failed_emails(emails):
        if type(emails) is str:
            emails = [emails]
        for email in emails:
            execute(f"UPDATE requests SET request_status = 0 WHERE request_email = '{email}'")