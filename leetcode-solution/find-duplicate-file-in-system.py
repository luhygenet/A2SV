class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        contents = defaultdict(list)
        for path in paths:
            path = path.split(" ")
            root = path[0]
            for folderAC in path[1:]:
                folderAC = folderAC.split(".txt")
                name = folderAC[0]
                content = folderAC[1]
                contents[content].append((root, name))
        output = []
        for k,v in contents.items():
            if len(v)>1:
                temp = []
                for root,name in v:
                    temp.append(root + "/" + name +".txt")
                output.append(temp)
        return (output)


