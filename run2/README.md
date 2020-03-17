Run #2
======

 - No. of TBR samples: 400,000
 - Job splitting: 400 jobs, 1K samples each
 - Simulation configuration: default (1 TBR sample = 10 batches, 10,000 particles each)
 - Sampling strategy: uniform
 - Hardware: Hypatia RCIF partition (4 nodes, 40 CPUs each)
 - Started: _pending_
 - Completed: _pending_


Notes:

 - Ignore `batch999`, it is just the first line of `batch0` that was used to test job deployment.
 - Discrete parameters were fixed in 4 configurations corresponding to:
   - `firstwall_coolant_material, blanket_coolant_material) == ('H2O', 'H2O')`
      for batches 0-99
   - `firstwall_coolant_material, blanket_coolant_material) == ('H2O', 'He')`
      for batches 100-199
   - `firstwall_coolant_material, blanket_coolant_material) == ('He', 'H2O')`
      for batches 200-299
   - `firstwall_coolant_material, blanket_coolant_material) == ('He', 'He')`
      for batches 300-399
 - Continuous parameters are sampled uniformly independently within each 100
   batch region. However, the between region their values were fixed so that
   `batchA == batchB iff A == B (mod 100)`.

