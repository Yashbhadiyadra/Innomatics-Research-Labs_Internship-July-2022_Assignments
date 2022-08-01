import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width) 
    dedented_text = textwrap.dedent(text=string) 
    result = wrapper.fill(text=dedented_text) 
    return result

if __name__ == '__main__':
    string, max_width = input("Enter the string: "), int(input("Enter the max-width: "))
    result = wrap(string, max_width)
    print(result)