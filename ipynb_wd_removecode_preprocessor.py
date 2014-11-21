from copy import deepcopy
from IPython.nbconvert.preprocessors import Preprocessor
from IPython.utils.traitlets import Unicode

class CherryPickingPreprocessor(Preprocessor):

    expression = Unicode('True', config=True, help="keep tags expression.")

    def preprocess(self, nb, resources):

        # Loop through each cell, remove cells that dont match the query.
        for worksheet in nb.worksheets:
            remove_indices = []
            for index, cell in enumerate(worksheet.cells):
              cm = cell['metadata']
              #html,pdf,slides = False,False,False
              cutcode_pdf, cutcode_html = False,False
              if 'cell_tags' in cm:
                if 'cutcode_pdf' in cm['cell_tags']: cutcode_pdf = cm['cell_tags']['cutcode_pdf']
                if 'cutcode_html' in cm['cell_tags']: cutcode_html = cm['cell_tags']['cutcode_html']

                #if 'html' in cm['cell_tags']: html = cm['cell_tags']['html']
                #if 'pdf' in cm['cell_tags']: pdf = cm['cell_tags']['pdf']
                #if 'slides' in cm['cell_tags']: slides=cm['cell_tags']['slides']
              #p#rint 'slides = %s' %slides
              #print 'pdf = %s' %pdf
              #print 'html = %s' %html
              #print 'expression = %s' %self.expression
              #test = eval(self.expression)
              #print 'test = %s' %test 
              if eval(self.expression) == True: #False:
                remove_indices.append(index)

            for index in remove_indices[::-1]:
                #del worksheet.cells[index]
                #del worksheet.cells[index].input
                #del worksheet.cells[index]['input']
                ic =  worksheet.cells[index]
                del ic.input

        resources['notebook_copy'] = deepcopy(nb)
        return nb, resources

"""
    def validate_cell_tags(self, cell):
        if 'cell_tags' in cell['metadata']:
            return self.eval_tag_expression(cell['metadata']['cell_tags'], self.expression)
        else: 
          return False # return True
       
    def eval_tag_expression(self, tags, expression):
        
        # Create the tags as True booleans.  This allows us to use python 
        # expressions.
        for tag in tags:
            tagtag = tags[tag]
            exec tag + " = tagtag"

        # Attempt to evaluate expression.  If a variable is undefined, define
        # the variable as false.
        try:
          res = eval(expression)
        except NameError as Error:
          #exec str(Error).split("'")[1] + " = False"
          #res = eval(expression)
          res = False
        return res



"""
