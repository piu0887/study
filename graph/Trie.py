# key 에는 해당 노드의 문자가 들어가고, child에는 자식노드가 포함
# data 는 문자열 종료를 알리는 flag (True/False로 구현할수있지만 돌아가는 일이 없게하기위해)
# 당노드에서 끝나는 문자열이 없을 경우 None으로 나둠

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data= data
        self.children = {}

class trie(object):
    def __init__(self):
        self.head = Node(None)
    
    #문자열 삽입
    def insert(self,string):
        curr_node = self.head
        #삽입할 string 각각의 문제에 대해 자식 Node를 만들며 내려간다.
        for char in string:
            #자식 Node들 중 같은 문자가 없으면 Node 새로 생성
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            # 같은 문자가 있으면 생성하지 않고, 해당노드로이동
            curr_node = curr_node.children[char]
        #문자열이 끝난 지점의 노드의 data값에 해당 문자열을 입력
        curr_node.data = string
    # 문자열이 존재 하는지 search

    def search(self, string) :
        curr_node = self.head
        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False
            
        #탐색이 끝난 후 해당 노드의 data값이 존재하면
        #문자가 포함되어있다는 뜻이다.
        if curr_node.data :
            return True
        else:
            return False
        
    # prefix단어로 시작하는 단어를 찾고 배열로 리턴하는 함수
    # BFS 방식으로 깊이를 늘려가며 prefix로 시작하는 문자열을 저장한 배열 반환
        
    def starts_with(self, prefix):
        curr_node = self.head
        words = []

        #prefix의 처음부터 마지막까지 탐색
        for p in prefix:
            # 만약 현재 노드의 자식노드중 문자에 해당하는 노드가 존재한다면
            if p in curr_node.children:
                # curr_node를 자식노드로 변경
                curr_node = curr_node.children[p]
            else:
                return None
            
        #prefix의 마지막 노드    
        curr_node = [curr_node]
        # 다음 노드를 저장할 배열
        next_node = []
        while True:
            # 현재 노드부터 탐색
            for node in curr_node:
                #만약 데이터가 있다면
                if node.data:
                    #word 배열에 추가
                    words.append(node.data)
                #현재 노드의 자신 노드 전부를 next_node 배열에 추가
                #list extend 와 expend 정리
                next_node.extend(list(node.children.values()))
            # 만약 다음 노드가 존재 한다면
            if len(next_node) != 0:
                # 다음노드들을 현재 노드로 변경
                curr_node = next_node
                # next_node는 다시 비워준다
                next_node = []
            else:
                #없으면 종료
                break

        return words
