# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def Macro1():
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(triad=OFF, 
        title=OFF, state=OFF, annotations=OFF, compass=OFF)
    session.graphicsOptions.setValues(backgroundStyle=SOLID, 
        backgroundColor='#FFFFFF')
    session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        CONTOURS_ON_DEF, ))
    session.viewports['Viewport: 1'].view.fitView()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=256.9, 
        farPlane=311.019, width=150.142, height=139.506, viewOffsetX=-11.6928, 
        viewOffsetY=1.04941)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=255.535, 
        farPlane=312.384, width=149.345, height=138.764, viewOffsetX=-10.4165, 
        viewOffsetY=-21.0369)
    session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
        variableLabel='SDV147', outputPosition=INTEGRATION_POINT, )
    session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
        variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(
        INVARIANT, 'Mises'), )
    session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
        variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(
        INVARIANT, 'Max. Principal (Abs)'), )
    session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
        variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(
        INVARIANT, 'Tresca'), )
    session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
        variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(
        INVARIANT, 'Max. Principal'), )
    session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
        variableLabel='SDV147', outputPosition=INTEGRATION_POINT, )
    session.printToFile(fileName='D:/1_Abaqus_Temp/Steel_PH/Cali/Energy', 
        format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))
    session.viewports['Viewport: 1'].view.fitView()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=246.565, 
        farPlane=321.355, width=177.799, height=92.369, viewOffsetX=-5.05932)
    session.viewports['Viewport: 1'].view.fitView()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=246.852, 
        farPlane=321.068, width=146.168, height=92.4765, viewOffsetX=-19.7784, 
        viewOffsetY=-0.241455)
    session.printToFile(fileName='D:/1_Abaqus_Temp/Steel_PH/Cali/Energy', 
        format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))


