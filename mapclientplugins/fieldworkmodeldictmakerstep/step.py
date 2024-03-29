'''
MAP Client Plugin Step
'''

from PySide6 import QtGui

from mapclient.mountpoints.workflowstep import WorkflowStepMountPoint


class FieldworkModelDictMakerStep(WorkflowStepMountPoint):
    '''
    Step for collating a fieldwork model into a new or existing 
    dictionary (fieldworkmodeldict).
    '''

    def __init__(self, location):
        super(FieldworkModelDictMakerStep, self).__init__('Fieldwork Model Dict Maker', location)
        self._configured = True  # A step cannot be executed until it has been configured.
        self._category = 'Fieldwork'
        # Add any other initialisation code here:
        self._icon = QtGui.QImage(':/fieldworkmodeldictmakerstep/images/fieldworkmodeldictmakericon.png')
        # Ports:
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'ju#fieldworkmodeldict'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'ju#fieldworkmodeldict'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'ju#fieldworkmodel'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'python#string'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'ju#fieldworkmodeldict'))

        self._gfDict = None
        self._gf = None
        self._gfName = None
        self._gfDict2 = None

    def execute(self):
        '''
        Add your code here that will kick off the execution of the step.
        Make sure you call the _doneExecution() method when finished.  This method
        may be connected up to a button in a widget for example.
        '''
        # Put your execute step code here before calling the '_doneExecution' method.
        if self._gfDict is None:
            self._gfDict = {}
        if self._gfName is not None:
            self._gfDict[self._gfName] = self._gf
        if self._gfDict2 is not None:
            self._gfDict.update(self._gfDict2)
        self._doneExecution()

    def setPortData(self, index, dataIn):
        '''
        Add your code here that will set the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        uses port for this step then the index can be ignored.
        '''
        if index == 1:
            self._gfDict = dataIn  # ju#fieldworkmodeldict
        elif index == 2:
            self._gf = dataIn  # ju#fieldworkmodel
        elif index == 3:
            self._gfName = dataIn  # string
        else:
            self._gfDict2 = dataIn

    def getPortData(self, index):
        '''
        Add your code here that will return the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        provides port for this step then the index can be ignored.
        '''
        return self._gfDict  # ju#fieldworkmodeldict

    def configure(self):
        '''
        This function will be called when the configure icon on the step is
        clicked.  It is appropriate to display a configuration dialog at this
        time.  If the conditions for the configuration of this step are complete
        then set:
            self._configured = True
        '''
        pass

    def getIdentifier(self):
        '''
        The identifier is a string that must be unique within a workflow.
        '''
        return 'FieldworkModelDictMaker'  # TODO: The string must be replaced with the step's unique identifier

    def setIdentifier(self, identifier):
        '''
        The framework will set the identifier for this step when it is loaded.
        '''
        pass  # TODO: Must actually set the step's identifier here

    def serialize(self):
        '''
        Add code to serialize this step to disk. Returns a json string for
        mapclient to serialise.
        '''
        return ''

    def deserialize(self, string):
        '''
        Add code to deserialize this step from disk. Parses a json string
        given by mapclient
        '''
        pass
