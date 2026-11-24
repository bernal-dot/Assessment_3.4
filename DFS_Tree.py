class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_complete_binary_tree(characters):
    if not characters:
        return None

    nodes = [TreeNode(ch) for ch in characters]
    for i in range(len(nodes)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(nodes):
            nodes[i].left = nodes[left_index]
        if right_index < len(nodes):
            nodes[i].right = nodes[right_index]
    return nodes[0]


def preorder(node, result):
    if node:
        result.append(node.value)
        preorder(node.left, result)
        preorder(node.right, result)


def inorder(node, result):
    if node:
        inorder(node.left, result)
        result.append(node.value)
        inorder(node.right, result)


def postorder(node, result):
    if node:
        postorder(node.left, result)
        postorder(node.right, result)
        result.append(node.value)


if __name__ == "__main__":
    # First Name + Last Name (change to "JELINA" if only first name was used in 3.5)
    name_letters = list("JELINABERNAL")
    root = build_complete_binary_tree(name_letters)

    pre_res, in_res, post_res = [], [], []
    preorder(root, pre_res)
    inorder(root, in_res)
    postorder(root, post_res)

    print("Input Characters:", " - ".join(name_letters))
    print("PreOrder (Root -> Left -> Right):", " - ".join(pre_res))
    print("InOrder  (Left -> Root -> Right):", " - ".join(in_res))
    print("PostOrder(Left -> Right -> Root):", " - ".join(post_res))