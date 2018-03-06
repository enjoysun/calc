class Node(object):
    """构造节点"""

    def __init__(self, item):
        self.element = item
        self.next = None


class SingleList(object):
    """构造单链表"""
    def __init__(self, headnode=None):
        """初始化一个单链表默认节点"""
        self.__head = headnode

    def is_empty(self):
        """是否为空"""
        return self.__head == None

    def length(self):
        """链表长度"""
        """定义游标来指向当前head"""
        cur = self.__head
        """定义长度变量记录长度，最好初始值为0"""
        count = 0

        while cur != None:
            cur = cur.next
            count += 1
        return count

    def list_each(self):
        """遍历单链表"""
        """定义游标"""
        cur = self.__head
        while cur != None:
            print(cur.element, end=",")
            cur = cur.next

    def append_node(self, item):
        """末尾追加一个节点"""
        """定义游标使游标指向末尾节点即可"""
        cur = self.__head
        if cur == None:
            self.__head = Node(item)
        else:
            while cur.next != None:
                cur = cur.next
            cur.next = Node(item)

    def insert_node(self, pos, item):
        """指定位置追加节点"""
        if not isinstance(pos, int):
            raise TypeError("位置参数必须为整数")
        cur = self.__head
        if self.length() <= pos:
            raise TypeError("超出索引")
        if pos == 0:
            next_node_next = self.__head
            self.__head = Node(item)
            self.__head.next = next_node_next
            return True
        count = 0
        while cur != None:
            """当前next地址"""
            next_cur = cur.next
            if count == pos-1:
                next_node = cur.next
                insert_node = Node(item)
                insert_node.next = next_cur
                cur.next = insert_node
                return True
            cur = cur.next
            count += 1

    def remove_node(self, item):
        """移除一个节点"""
        cur = self.__head
        """使用双游标来标记一前一后节点"""
        pre = None
        while cur != Node:
            if cur.element == item:
                """处理头结点和列表只有一个元素特殊状况"""
                if cur == self.__head:
                    self.__head = cur.next
                    return True
                else:
                    pre.next = cur.next
                    return True
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        """查看节点按是否存在"""
        cur = self.__head
        while cur != None:
            if cur.element == item:
                return True
            cur = cur.next
        return False


if __name__ == "__main__":
    ll = SingleList()
    ll.append_node(1)
    ll.append_node(2)
    ll.append_node(3)
    print(ll.is_empty())
    print(ll.length())
    ll.insert_node(0, 5)
    print(ll.search(1))
    ll.list_each()
    print("\n")
    ll.remove_node(2)
    ll.list_each()






