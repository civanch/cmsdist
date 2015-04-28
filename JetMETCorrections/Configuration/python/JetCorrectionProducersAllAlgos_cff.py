import FWCore.ParameterSet.Config as cms

from JetMETCorrections.Configuration.JetCorrectionServicesAllAlgos_cff import *
from JetMETCorrections.Configuration.JetCorrectionProducers_cff import *

# L1 Correction Producers
ak7CaloJetsL1 = ak4CaloJetsL1.clone( src = 'ak7CaloJets' )
kt4CaloJetsL1 = ak4CaloJetsL1.clone( src = 'kt4CaloJets' )
kt6CaloJetsL1 = ak4CaloJetsL1.clone( src = 'kt6CaloJets' )
ic5CaloJetsL1 = ak4CaloJetsL1.clone( src = 'ic5CaloJets' )

ak1PFJetsL1 = ak4PFJetsL1.clone( src = 'ak1PFJets' )
ak1PFCHSJetsL1 = ak4PFCHSJetsL1.clone( src = 'ak1PFCHSJets' )
ak2PFJetsL1 = ak4PFJetsL1.clone( src = 'ak2PFJets' )
ak2PFCHSJetsL1 = ak4PFCHSJetsL1.clone( src = 'ak2PFCHSJets' )
ak3PFJetsL1 = ak4PFJetsL1.clone( src = 'ak3PFJets' )
ak3PFCHSJetsL1 = ak4PFCHSJetsL1.clone( src = 'ak3PFCHSJets' )
ak5PFJetsL1 = ak4PFJetsL1.clone( src = 'ak5PFJets' )
ak5PFCHSJetsL1 = ak4PFCHSJetsL1.clone( src = 'ak5PFCHSJets' )
ak6PFJetsL1 = ak4PFJetsL1.clone( src = 'ak6PFJets' )
ak6PFCHSJetsL1 = ak4PFCHSJetsL1.clone( src = 'ak6PFCHSJets' )
ak7PFJetsL1 = ak4PFJetsL1.clone( src = 'ak7PFJets' )
ak7PFCHSJetsL1 = ak4PFCHSJetsL1.clone( src = 'ak7PFCHSJets' )
ak8PFJetsL1 = ak4PFJetsL1.clone( src = 'ak8PFJets' )
ak8PFCHSJetsL1 = ak4PFCHSJetsL1.clone( src = 'ak8PFCHSJets' )
ak9PFJetsL1 = ak4PFJetsL1.clone( src = 'ak9PFJets' )
ak9PFCHSJetsL1 = ak4PFCHSJetsL1.clone( src = 'ak9PFCHSJets' )
ak10PFJetsL1 = ak4PFJetsL1.clone( src = 'ak10PFJets' )
ak10PFCHSJetsL1 = ak4PFCHSJetsL1.clone( src = 'ak10PFCHSJets' )
kt4PFJetsL1 = ak4PFJetsL1.clone( src = 'kt4PFJets' )
kt6PFJetsL1 = ak4PFJetsL1.clone( src = 'kt6PFJets' )
ic5PFJetsL1 = ak4PFJetsL1.clone( src = 'ic5PFJets' )


# L2L3 Correction Producers
ak7CaloJetsL2 = ak7CaloJetsL1.clone(correctors = ['ak7CaloL2Relative'])
kt4CaloJetsL2 = kt4CaloJetsL1.clone(correctors = ['kt4CaloL2Relative'])
kt6CaloJetsL2 = kt6CaloJetsL1.clone(correctors = ['kt6CaloL2Relative'])
ic5CaloJetsL2 = ic5CaloJetsL1.clone(correctors = ['ic5CaloL2Relative'])

ak1PFJetsL2 = ak1PFJetsL1.clone(correctors = ['ak1PFL2Relative'])
ak1PFCHSJetsL2 = ak1PFCHSJetsL1.clone(correctors = ['ak1PFCHSL2Relative'])
ak2PFJetsL2 = ak2PFJetsL1.clone(correctors = ['ak2PFL2Relative'])
ak2PFCHSJetsL2 = ak2PFCHSJetsL1.clone(correctors = ['ak2PFCHSL2Relative'])
ak3PFJetsL2 = ak3PFJetsL1.clone(correctors = ['ak3PFL2Relative'])
ak3PFCHSJetsL2 = ak3PFCHSJetsL1.clone(correctors = ['ak3PFCHSL2Relative'])
ak5PFJetsL2 = ak5PFJetsL1.clone(correctors = ['ak5PFL2Relative'])
ak5PFCHSJetsL2 = ak5PFCHSJetsL1.clone(correctors = ['ak5PFCHSL2Relative'])
ak6PFJetsL2 = ak6PFJetsL1.clone(correctors = ['ak6PFL2Relative'])
ak6PFCHSJetsL2 = ak6PFCHSJetsL1.clone(correctors = ['ak6PFCHSL2Relative'])
ak7PFJetsL2 = ak7PFJetsL1.clone(correctors = ['ak7PFL2Relative'])
ak7PFCHSJetsL2 = ak7PFCHSJetsL1.clone(correctors = ['ak7PFCHSL2Relative'])
ak8PFJetsL2 = ak8PFJetsL1.clone(correctors = ['ak8PFL2Relative'])
ak8PFCHSJetsL2 = ak8PFCHSJetsL1.clone(correctors = ['ak8PFCHSL2Relative'])
ak9PFJetsL2 = ak9PFJetsL1.clone(correctors = ['ak9PFL2Relative'])
ak9PFCHSJetsL2 = ak9PFCHSJetsL1.clone(correctors = ['ak9PFCHSL2Relative'])
ak10PFJetsL2 = ak10PFJetsL1.clone(correctors = ['ak10PFL2Relative'])
ak10PFCHSJetsL2 = ak10PFCHSJetsL1.clone(correctors = ['ak10PFCHSL2Relative'])
kt4PFJetsL2 = kt4PFJetsL1.clone(correctors = ['kt4PFL2Relative'])
kt6PFJetsL2 = kt6PFJetsL1.clone(correctors = ['kt6PFL2Relative'])
ic5PFJetsL2 = ic5PFJetsL1.clone(correctors = ['ic5PFL2Relative'])

ak4JPTJetsL2 = ak4JPTJetsL1.clone(correctors = ['ak4JPTL2Relative'])
ak4TrackJetsL2 = ak4TrackJetsL1.clone(correctors = ['ak5TRKL2Relative'])

# L2L3 Correction Producers
ak7CaloJetsL2L3 = ak7CaloJetsL1.clone(correctors = ['ak7CaloL2L3'])
kt4CaloJetsL2L3 = kt4CaloJetsL1.clone(correctors = ['kt4CaloL2L3'])
kt6CaloJetsL2L3 = kt6CaloJetsL1.clone(correctors = ['kt6CaloL2L3'])
ic5CaloJetsL2L3 = ic5CaloJetsL1.clone(correctors = ['ic5CaloL2L3'])

ak1PFJetsL2L3 = ak1PFJetsL1.clone(correctors = ['ak1PFL2L3'])
ak1PFCHSJetsL2L3 = ak1PFCHSJetsL1.clone(correctors = ['ak1PFCHSL2L3'])
ak2PFJetsL2L3 = ak2PFJetsL1.clone(correctors = ['ak2PFL2L3'])
ak2PFCHSJetsL2L3 = ak2PFCHSJetsL1.clone(correctors = ['ak2PFCHSL2L3'])
ak3PFJetsL2L3 = ak3PFJetsL1.clone(correctors = ['ak3PFL2L3'])
ak3PFCHSJetsL2L3 = ak3PFCHSJetsL1.clone(correctors = ['ak3PFCHSL2L3'])
ak5PFJetsL2L3 = ak5PFJetsL1.clone(correctors = ['ak5PFL2L3'])
ak5PFCHSJetsL2L3 = ak5PFCHSJetsL1.clone(correctors = ['ak5PFCHSL2L3'])
ak6PFJetsL2L3 = ak6PFJetsL1.clone(correctors = ['ak6PFL2L3'])
ak6PFCHSJetsL2L3 = ak6PFCHSJetsL1.clone(correctors = ['ak6PFCHSL2L3'])
ak7PFJetsL2L3 = ak7PFJetsL1.clone(correctors = ['ak7PFL2L3'])
ak7PFCHSJetsL2L3 = ak7PFCHSJetsL1.clone(correctors = ['ak7PFCHSL2L3'])
ak8PFJetsL2L3 = ak8PFJetsL1.clone(correctors = ['ak8PFL2L3'])
ak8PFCHSJetsL2L3 = ak8PFCHSJetsL1.clone(correctors = ['ak8PFCHSL2L3'])
ak9PFJetsL2L3 = ak9PFJetsL1.clone(correctors = ['ak9PFL2L3'])
ak9PFCHSJetsL2L3 = ak9PFCHSJetsL1.clone(correctors = ['ak9PFCHSL2L3'])
ak10PFJetsL2L3 = ak10PFJetsL1.clone(correctors = ['ak10PFL2L3'])
ak10PFCHSJetsL2L3 = ak10PFCHSJetsL1.clone(correctors = ['ak10PFCHSL2L3'])
kt4PFJetsL2L3 = kt4PFJetsL1.clone(correctors = ['kt4PFL2L3'])
kt6PFJetsL2L3 = kt6PFJetsL1.clone(correctors = ['kt6PFL2L3'])
ic5PFJetsL2L3 = ic5PFJetsL1.clone(correctors = ['ic5PFL2L3'])

ak4JPTJetsL2L3 = ak4JPTJetsL1.clone(correctors = ['ak4JPTL2L3'])
ak4TrackJetsL2L3 = ak4TrackJetsL1.clone(correctors = ['ak5TRKL2L3'])

# L1L2L3 Correction Producers
ak7CaloJetsL1L2L3 = ak7CaloJetsL1.clone(correctors = ['ak7CaloL1L2L3'])
kt4CaloJetsL1L2L3 = kt4CaloJetsL1.clone(correctors = ['kt4CaloL1L2L3'])
kt6CaloJetsL1L2L3 = kt6CaloJetsL1.clone(correctors = ['kt6CaloL1L2L3'])
ic5CaloJetsL1L2L3 = ic5CaloJetsL1.clone(correctors = ['ic5CaloL1L2L3'])

ak1PFJetsL1L2L3 = ak1PFJetsL1.clone(correctors = ['ak1PFL1L2L3'])
ak1PFCHSJetsL1L2L3 = ak1PFCHSJetsL1.clone(correctors = ['ak1PFCHSL1L2L3'])
ak2PFJetsL1L2L3 = ak2PFJetsL1.clone(correctors = ['ak2PFL1L2L3'])
ak2PFCHSJetsL1L2L3 = ak2PFCHSJetsL1.clone(correctors = ['ak2PFCHSL1L2L3'])
ak3PFJetsL1L2L3 = ak3PFJetsL1.clone(correctors = ['ak3PFL1L2L3'])
ak3PFCHSJetsL1L2L3 = ak3PFCHSJetsL1.clone(correctors = ['ak3PFCHSL1L2L3'])
ak5PFJetsL1L2L3 = ak5PFJetsL1.clone(correctors = ['ak5PFL1L2L3'])
ak5PFCHSJetsL1L2L3 = ak5PFCHSJetsL1.clone(correctors = ['ak5PFCHSL1L2L3'])
ak6PFJetsL1L2L3 = ak6PFJetsL1.clone(correctors = ['ak6PFL1L2L3'])
ak6PFCHSJetsL1L2L3 = ak6PFCHSJetsL1.clone(correctors = ['ak6PFCHSL1L2L3'])
ak7PFJetsL1L2L3 = ak7PFJetsL1.clone(correctors = ['ak7PFL1L2L3'])
ak7PFCHSJetsL1L2L3 = ak7PFCHSJetsL1.clone(correctors = ['ak7PFCHSL1L2L3'])
ak8PFJetsL1L2L3 = ak8PFJetsL1.clone(correctors = ['ak8PFL1L2L3'])
ak8PFCHSJetsL1L2L3 = ak8PFCHSJetsL1.clone(correctors = ['ak8PFCHSL1L2L3'])
ak9PFJetsL1L2L3 = ak9PFJetsL1.clone(correctors = ['ak9PFL1L2L3'])
ak9PFCHSJetsL1L2L3 = ak9PFCHSJetsL1.clone(correctors = ['ak9PFCHSL1L2L3'])
ak10PFJetsL1L2L3 = ak10PFJetsL1.clone(correctors = ['ak10PFL1L2L3'])
ak10PFCHSJetsL1L2L3 = ak10PFCHSJetsL1.clone(correctors = ['ak10PFCHSL1L2L3'])
kt4PFJetsL1L2L3 = kt4PFJetsL1.clone(correctors = ['kt4PFL1L2L3'])
kt6PFJetsL1L2L3 = kt6PFJetsL1.clone(correctors = ['kt6PFL1L2L3'])
ic5PFJetsL1L2L3 = ic5PFJetsL1.clone(correctors = ['ic5PFL1L2L3'])

ak4JPTJetsL1L2L3 = ak4JPTJetsL1.clone(correctors = ['ak4JPTL1L2L3'])
ak4TrackJetsL1L2L3 = ak4TrackJetsL1.clone(correctors = ['ak5TRKL1L2L3'])

# L2L3L6 CORRECTION PRODUCERS
ak7CaloJetsL2L3L6 = ak7CaloJetsL1.clone(correctors = ['ak7CaloL2L3L6'])
kt4CaloJetsL2L3L6 = kt4CaloJetsL1.clone(correctors = ['kt4CaloL2L3L6'])
kt6CaloJetsL2L3L6 = kt6CaloJetsL1.clone(correctors = ['kt6CaloL2L3L6'])
ic5CaloJetsL2L3L6 = ic5CaloJetsL1.clone(correctors = ['ic5CaloL2L3L6'])

ak7PFJetsL2L3L6 = ak7PFJetsL1.clone(correctors = ['ak7PFL2L3L6'])
kt4PFJetsL2L3L6 = kt4PFJetsL1.clone(correctors = ['kt4PFL2L3L6'])
kt6PFJetsL2L3L6 = kt6PFJetsL1.clone(correctors = ['kt6PFL2L3L6'])
ic5PFJetsL2L3L6 = ic5PFJetsL1.clone(correctors = ['ic5PFL2L3L6'])


# L1L2L3L6 CORRECTION PRODUCERS
ak7CaloJetsL1L2L3L6 = ak7CaloJetsL1.clone(correctors = ['ak7CaloL1L2L3L6'])
kt4CaloJetsL1L2L3L6 = kt4CaloJetsL1.clone(correctors = ['kt4CaloL1L2L3L6'])
kt6CaloJetsL1L2L3L6 = kt6CaloJetsL1.clone(correctors = ['kt6CaloL1L2L3L6'])
ic5CaloJetsL1L2L3L6 = ic5CaloJetsL1.clone(correctors = ['ic5CaloL1L2L3L6'])

ak7PFJetsL1L2L3L6 = ak7PFJetsL1.clone(correctors = ['ak7PFL1L2L3L6'])
kt4PFJetsL1L2L3L6 = kt4PFJetsL1.clone(correctors = ['kt4PFL1L2L3L6'])
kt6PFJetsL1L2L3L6 = kt6PFJetsL1.clone(correctors = ['kt6PFL1L2L3L6'])
ic5PFJetsL1L2L3L6 = ic5PFJetsL1.clone(correctors = ['ic5PFL1L2L3L6'])