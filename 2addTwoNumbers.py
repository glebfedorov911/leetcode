class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_reversed = self.reverse_listnode(l1)
        l2_reversed = self.reverse_listnode(l2)

        l1_num = int(''.join(map(str, l1_reversed)))
        l2_num = int(''.join(map(str, l2_reversed)))

        l3_reversed = [int(i) for i in str(l1_num+l2_num)]
        self.create_listnode(l3_reversed)

    def reverse_listnode(self, l: list):
        l_reversed = []
        while True:
            if not l:
                break
            l_reversed.append(l.val)
            l = l.next
        
        return l_reversed[::-1]

    def create_listnode(self, l: list):
        ln1 = ListNode(val=l[-1])
        for i in range(0, len(l)-1):
            lnn = ListNode(val=l[i])
            ln1.next = lnn
        print(ln1)
