class Solution(object):
    #O(n*k) Time | O(k) Space, where k is length of longest email and n is length of emails
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        uniqueEmails = set()
        for email in emails:
            finalEmail = self.getFinalEmail(email)
            uniqueEmails.add(finalEmail)
        return len(uniqueEmails)
        
    # O(k) Time | O(k) Space, where k is length of email
    def getFinalEmail(self, email):
        localName = email.split('@')[0]
        domainName = email.split('@')[1]
        local = localName.split('+')[0].replace('.', '')
        return local + '@' + domainName
