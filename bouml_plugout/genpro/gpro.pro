TEMPLATE	= app
TARGET		= gpro
CONFIG		+=  warn_on qt
DEFINES		= WITHCPP
HEADERS		= ./UmlClassItem.h \
		  ./UmlBaseNode.h \
		  ./UmlBaseDeployment.h \
		  ./UmlOperation.h \
		  ./aVisibility.h \
		  ./UmlBaseClassMember.h \
		  ./UmlBaseCollaborationDiagram.h \
		  ./UmlDeploymentView.h \
		  ./UmlBaseUseCaseDiagram.h \
		  ./UmlBaseSequenceDiagram.h \
		  ./UmlParameter.h \
		  ./JavaSettingsCmd.h \
		  ./UmlBaseNcRelation.h \
		  ./UmlUseCaseView.h \
		  ./UmlExtraClassMember.h \
		  ./anItemKind.h \
		  ./UmlBaseDiagram.h \
		  ./UmlClassDiagram.h \
		  ./UmlClassMember.h \
		  ./UmlBaseComponentView.h \
		  ./CmdFamily.h \
		  ./JavaSettings.h \
		  ./UmlBaseAttribute.h \
		  ./UmlItem.h \
		  ./UmlBaseExtraClassMember.h \
		  ./UmlBaseRelation.h \
		  ./UmlBuiltin.h \
		  ./UmlBaseActualParameter.h \
		  ./UmlBaseArtifact.h \
		  ./UmlFormalParameter.h \
		  ./IdlSettingsCmd.h \
		  ./UmlBaseComponentDiagram.h \
		  ./UmlRelation.h \
		  ./UmlPackage.h \
		  ./UmlBaseUseCaseView.h \
		  ./UmlBaseClassView.h \
		  ./CppSettings.h \
		  ./UmlSequenceDiagram.h \
		  ./UmlTypeSpec.h \
		  ./UmlBaseClassDiagram.h \
		  ./UmlArtifact.h \
		  ./UmlUseCaseDiagram.h \
		  ./UmlAttribute.h \
		  ./UmlBaseOperation.h \
		  ./IdlSettings.h \
		  ./UmlNode.h \
		  ./aDirection.h \
		  ./UmlActualParameter.h \
		  ./UmlSettingsCmd.h \
		  ./UmlDeploymentDiagram.h \
		  ./PackageGlobalCmd.h \
		  ./UmlBaseUseCase.h \
		  ./UmlComponent.h \
		  ./UmlSettings.h \
		  ./UmlClassView.h \
		  ./UmlBaseDeploymentView.h \
		  ./UmlComponentView.h \
		  ./UmlNcRelation.h \
		  ./UmlClass.h \
		  ./MiscGlobalCmd.h \
		  ./CppSettingsCmd.h \
		  ./UmlComponentDiagram.h \
		  ./UmlBaseItem.h \
		  ./UmlCollaborationDiagram.h \
		  ./UmlCom.h \
		  ./OnInstanceCmd.h \
		  ./Dialog.h \
		  ./UmlBaseClass.h \
		  ./UmlBaseClassItem.h \
		  ./UmlBaseFormalParameter.h \
		  ./UmlBasePackage.h \
		  ./ClassGlobalCmd.h \
		  ./UmlDiagram.h \
		  ./aRelationKind.h \
		  ./SmallPushButton.h \
		  ./UmlStereotype.h \
		  ./UmlBaseDeploymentDiagram.h \
		  ./UmlBaseComponent.h \
		  ./UmlUseCase.h
SOURCES		= ./UmlClassItem.cpp \
		  ./UmlBaseNode.cpp \
		  ./UmlBaseDeployment.cpp \
		  ./UmlOperation.cpp \
		  ./aVisibility.cpp \
		  ./UmlBaseClassMember.cpp \
		  ./UmlBaseCollaborationDiagram.cpp \
		  ./UmlDeploymentView.cpp \
		  ./UmlBaseUseCaseDiagram.cpp \
		  ./UmlBaseSequenceDiagram.cpp \
		  ./UmlParameter.cpp \
		  ./JavaSettingsCmd.cpp \
		  ./UmlBaseNcRelation.cpp \
		  ./UmlUseCaseView.cpp \
		  ./UmlExtraClassMember.cpp \
		  ./anItemKind.cpp \
		  ./UmlBaseDiagram.cpp \
		  ./UmlClassDiagram.cpp \
		  ./UmlClassMember.cpp \
		  ./UmlBaseComponentView.cpp \
		  ./CmdFamily.cpp \
		  ./JavaSettings.cpp \
		  ./UmlBaseAttribute.cpp \
		  ./UmlItem.cpp \
		  ./UmlBaseExtraClassMember.cpp \
		  ./UmlBaseRelation.cpp \
		  ./UmlBuiltin.cpp \
		  ./UmlBaseActualParameter.cpp \
		  ./UmlBaseArtifact.cpp \
		  ./UmlFormalParameter.cpp \
		  ./IdlSettingsCmd.cpp \
		  ./UmlBaseComponentDiagram.cpp \
		  ./UmlRelation.cpp \
		  ./UmlPackage.cpp \
		  ./Main.cpp \
		  ./UmlBaseUseCaseView.cpp \
		  ./UmlBaseClassView.cpp \
		  ./CppSettings.cpp \
		  ./UmlSequenceDiagram.cpp \
		  ./UmlTypeSpec.cpp \
		  ./UmlBaseClassDiagram.cpp \
		  ./UmlArtifact.cpp \
		  ./UmlUseCaseDiagram.cpp \
		  ./UmlAttribute.cpp \
		  ./UmlBaseOperation.cpp \
		  ./IdlSettings.cpp \
		  ./UmlNode.cpp \
		  ./aDirection.cpp \
		  ./UmlActualParameter.cpp \
		  ./UmlSettingsCmd.cpp \
		  ./UmlDeploymentDiagram.cpp \
		  ./PackageGlobalCmd.cpp \
		  ./UmlBaseUseCase.cpp \
		  ./UmlComponent.cpp \
		  ./UmlSettings.cpp \
		  ./UmlClassView.cpp \
		  ./UmlBaseDeploymentView.cpp \
		  ./UmlComponentView.cpp \
		  ./UmlNcRelation.cpp \
		  ./UmlClass.cpp \
		  ./MiscGlobalCmd.cpp \
		  ./CppSettingsCmd.cpp \
		  ./UmlComponentDiagram.cpp \
		  ./UmlBaseItem.cpp \
		  ./UmlCollaborationDiagram.cpp \
		  ./UmlCom.cpp \
		  ./OnInstanceCmd.cpp \
		  ./Dialog.cpp \
		  ./UmlBaseClass.cpp \
		  ./UmlBaseClassItem.cpp \
		  ./UmlBaseFormalParameter.cpp \
		  ./UmlBasePackage.cpp \
		  ./ClassGlobalCmd.cpp \
		  ./UmlDiagram.cpp \
		  ./aRelationKind.cpp \
		  ./SmallPushButton.cpp \
		  ./UmlStereotype.cpp \
		  ./UmlBaseDeploymentDiagram.cpp \
		  ./UmlBaseComponent.cpp \
		  ./UmlUseCase.cpp
QT += network  qt3support
