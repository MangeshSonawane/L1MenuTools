# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: cmsDriver.py l1Ntuple -s RAW2DIGI --python_filename=mc.py -n -1 --no_output --era=Run3 --mc --conditions=140X_mcRun3_2024_realistic_v14 --customise=L1Trigger/Configuration/customiseReEmul.L1TReEmulMCFromRAWSimHcalTP --customise=L1Trigger/L1TNtuples/customiseL1Ntuple.L1NtupleRAWEMUGEN_MC --filein=/store/mc/Run3Winter24Digi/SingleNeutrino_Pt-2To20-gun/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/2540000/038bda40-23b3-4038-a546-6397626ae3e2.root

import FWCore.ParameterSet.Config as cms
from Configuration.Eras.Era_Run3_cff import Run3
import FWCore.ParameterSet.VarParsing as VarParsing # ADDED                                                                                                          
import FWCore.Utilities.FileUtils as FileUtils # ADDED  

process = cms.Process('RAW2DIGI',Run3)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

# ADDED                                                                                                                                           
options = VarParsing.VarParsing ('analysis')
# get and parse the command line arguments                                                                                                                  

options.register('skipEvents',
                 0,
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.int,
                 "Number of events to skip")
options.register('outFile',
                 'L1Ntuple.root',
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.string,
                 'Output file')

options.parseArguments()

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.maxEvents)
)

process.MessageLogger.suppressWarning = cms.untracked.vstring(
    'l1PhaseIITree', 'l1UpgradeTfMuonEmuTree', 'l1CaloTowerTree',
    'l1UpgradeTfMuonTree','l1UpgradeTree','l1HOTree', 'l1Phase2CaloTree')

# Input source                                                                                                                                  
process.source = cms.Source("PoolSource",
    skipEvents = cms.untracked.uint32(options.skipEvents), #added                                                          
    fileNames = cms.untracked.vstring(options.inputFiles),
    secondaryFileNames = cms.untracked.vstring()
)
# end ADDED  

process.options = cms.untracked.PSet(
    #FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    #SkipEvent = cms.untracked.vstring(),
    accelerators = cms.untracked.vstring('*'),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    makeTriggerResults = cms.obsolete.untracked.bool,
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('l1Ntuple nevts:-1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '140X_mcRun3_2024_realistic_v14', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.endjob_step = cms.EndPath(process.endOfProcess)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.endjob_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from L1Trigger.Configuration.customiseReEmul
from L1Trigger.Configuration.customiseReEmul import L1TReEmulMCFromRAWSimHcalTP 

#call to customisation function L1TReEmulMCFromRAWSimHcalTP imported from L1Trigger.Configuration.customiseReEmul
process = L1TReEmulMCFromRAWSimHcalTP(process)

# Automatic addition of the customisation function from L1Trigger.L1TNtuples.customiseL1Ntuple
from L1Trigger.L1TNtuples.customiseL1Ntuple import L1NtupleRAWEMUGEN_MC 

#call to customisation function L1NtupleRAWEMUGEN_MC imported from L1Trigger.L1TNtuples.customiseL1Ntuple
process = L1NtupleRAWEMUGEN_MC(process)

# End of customisation functions


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
