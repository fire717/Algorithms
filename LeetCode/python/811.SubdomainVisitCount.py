#80ms 72%
class Solution:   
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        domain_dict = {}
        for d in cpdomains:
            times, full_domain = d.split(' ')
            times = int(times)
            d_list = full_domain.split('.')
            d_len = len(d_list)
            if d_len == 1:
                domain_dict[d_list[0]] = domain_dict.get(d_list[0],0) + times
            elif d_len == 2:
                domain_dict[full_domain] = domain_dict.get(full_domain,0) + times
                domain_dict[d_list[1]] = domain_dict.get(d_list[1],0) + times
            else:
                domain2 = d_list[1]+'.'+d_list[2] 
                domain1 = d_list[2]
                domain_dict[full_domain] = domain_dict.get(full_domain,0) + times
                domain_dict[domain2] = domain_dict.get(domain2,0) + times
                domain_dict[domain1] = domain_dict.get(domain1,0) + times
        res = [str(v)+' '+k for k,v in domain_dict.items()]
        return res
