import gradio as gr
import ast
import random

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

def append_card(add_list, add_front, add_back):
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

    for  i in range (len(lists[list]['flashcards'])):
        if lists[list]['flashcards'][i][0]==add_front and lists[list]['flashcards'][i][0]==add_back:
            return(add_list, add_front, add_back,"There is already another card with those value")
    
    lists[list]['flashcards'].append([add_front, add_back])
    set_lists(lists)
    return(add_list,'','','Done!')

def delete(add_list, add_front, add_back):
    if (add_list==''):
        return(add_list, add_front, add_back,'Please insert the list where you want to delete the flashcard')
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

    for  i in range (len(lists[list]['flashcards'])):
        if lists[list]['flashcards'][i][0]==add_front and lists[list]['flashcards'][i][1]==add_back:
            lists[list]['flashcards'].pop(i)
            set_lists(lists)
            return(add_list, '', '',"Done")
    

    return(add_list,add_front, add_back,'There is no card in that list with that value')

def remove(add_list):
    if (add_list==''):
        return(add_list, add_front, add_back,'Please insert the list where you want to add the flashcard')

    lists=get_lists()
    list=None
    for i in range(len(lists)):
        if lists[i]['name']==add_list:
            list=i
            break
    if list is None:
        return(add_list, add_front, add_back,"There isn't a list with that name")

    lists.pop(i)
    set_lists(lists)
    return('','','','Done!')

def get_card(list):
    if (add_list==''):
        return(add_list, add_front, add_back,'Please insert the list where you want to add the flashcard')

    lists=get_lists()
    list=None
    for i in range(len(lists)):
        if lists[i]['name']==add_list:
            list=i
            break
    if list is None:
        return(add_list, add_front, add_back,"There isn't a list with that name")
#TODO







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
                    random_card=gr.Button("flashcared")
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
                    remove_list=gr.Button("Remove list")
        create_list.click(fn=append_list, inputs=[add_list], outputs=[add_list, add_front, add_back, add_result])   
        add_card.click(fn=append_card, inputs=[add_list, add_front, add_back], outputs=[add_list, add_front, add_back, add_result])
        delete_card.click(fn=delete, inputs=[add_list, add_front, add_back], outputs=[add_list, add_front, add_back, add_result])
        remove_list.click(fn=remove, inputs=[add_list], outputs=[add_list, add_front, add_back, add_result])
        random_card.click(fn=get_card, inputs=[list], outputs=[list, front, back])



    demo.launch(share=False)
