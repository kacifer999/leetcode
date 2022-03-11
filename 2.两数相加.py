class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
  def addTwoNumbers(self, l1, l2):
    result = node = ListNode()
    q = 0
    while l1 or l2:
      x = l1.val if l1 else 0
      y = l2.val if l2 else 0
      q,r = divmod(x + y + q, 10)
      node.next = ListNode(r)
      node = node.next
      
      if l1:
        l1 = l1.next
      if l2:
        l2 = l2.next
    if q > 0:
      node.next = ListNode(q)
    return result.next

  
#######
def assign_node(lis):
  node = None
  for value in (reversed(lis)):
    node = ListNode(value,node)
  return node

def print_node(node):
  string = ''
  while True:
    string += f'{node.val}'
    node = node.next
    if node == None:
      print(string)
      break
    else:
      string += ' → '

print_node(Solution().addTwoNumbers(assign_node([9,9,3]),assign_node([9,9,9])))
