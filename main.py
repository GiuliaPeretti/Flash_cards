import gradio as gr
import ast

def get_lists():
    with open('lists.json', 'r') as f:
        lists=f.read()
    return(ast.literal_eval(lists))
    
def set_lists(lists):
    lists=str(lists)
    lists=lists.replace("'",'"')
    with open('lists.json', 'w') as f:
        f.write(lists   )

def append_list(add_list):
    lists=get_lists()
    lists.append({"name": add_list, "flashcards": []})
    set_lists(lists)
    return('','','','Done!')

def append_card(add_list, add_front, add_back, add_result):
    if (add_list==''):
        return(add_list, add_front, add_back,'Please insert the list where you want to add the flashcard')
    if add_front=='':
        return(add_list, add_front, add_back,'Please insert the front of the card')
    if add_back=='':
        return(add_list, add_front, add_back,'Please insert the back of the card')
    lists=get_lists()
    list=None
    for i in range(len(lists)):
        if lists[i]['name']==add_list:
            list=i
            break
    if list is None:
        return(add_list, add_front, add_back,"There isn't a list with that name")
    lists[i]['flashcards'].append[add_front, add_back]
    set_lists(lists)
    return(add_list,'','','Done!')












if __name__=='__main__':
    with gr.Blocks() as demo:
        gr.Markdown("# Flash cards")
        with gr.Row():
            with gr.Column():
                gr.Markdown("## Practice")
                list=gr.Textbox(label="List: ")
                front=gr.Textbox(label="Front: ")
                back=gr.Textbox(label="Back: ")
                result=gr.Textbox(label="Result")
                with gr.Row():
                    check=gr.Button("Check")
            with gr.Column():
                gr.Markdown("## Edit lists")
                add_list=gr.Textbox(label="List: ")
                add_front=gr.Textbox(label="Front: ")
                add_back=gr.Textbox(label="Back: ")
                add_result=gr.Textbox(label="Result")
                with gr.Row():
                    create_list=gr.Button("Create List")
                    add_card=gr.Button("Add card")
                    delete_card=gr.Button("Delete card")
                    remove=gr.Button("Remove list")
        create_list.click(fn=append_list, inputs=[add_list], outputs=[add_list, add_front, add_back, add_result])   
        add_card.click(append_card, inputs=[add_list, add_front, add_back, add_result], outputs=[add_list, add_front, add_back, add_result])




    demo.launch(share=False)
