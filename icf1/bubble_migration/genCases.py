import casefoam


case =  [['interFoam','interIsoFoam','interFlow']]


def update_solver(solverName):
        return {'system/controlDict': { "application": solverName}}

def update_CFL(x):
    return  {'system/controlDict':
            {'maxDeltaT': str(x)}}

def updateBlockMesh(x):
    return  {'system/blockMeshDict': {
            'blocks': ['hex',
                   [0, 1, 2, 3, 4, 5, 6, 7],
                   '(%s %s 1)' % (x , x),
                   'simpleGrading',
                   '(1 1 1)']}}

data = {'interFoam': update_solver("interFoam"),
        'interIsoFoam': update_solver("interIsoFoam"),
        'interFlow':update_solver("interFlow")
        }

casefoam.mkCases('bubble_migration', case, data, 'tree',writeDir='Cases')