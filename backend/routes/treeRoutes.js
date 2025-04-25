// backend/routes/treeRoutes.js
const express = require('express');
const router = express.Router();
const Tree = require('../models/Tree');
const User = require('../models/User');

// Plant a real tree and update virtual city
router.post('/plant-tree', async (req, res) => {
  try {
    const { userId, treeType, location } = req.body;
    
    // Save real tree planting
    const newTree = new Tree({
      userId,
      type: treeType,
      location: {
        type: 'Point',
        coordinates: [location.longitude, location.latitude]
      },
      plantedAt: new Date()
    });
    await newTree.save();
    
    // Update user's virtual city
    const user = await User.findById(userId);
    const treeBenefits = calculateTreeBenefits(treeType);
    
    user.virtualCity.treesPlanted++;
    user.virtualCity.airQuality += treeBenefits.airQuality;
    user.virtualCity.biodiversity += treeBenefits.biodiversity;
    user.virtualCity.coins += treeBenefits.coins;
    
    await user.save();
    
    // Update leaderboard
    updateLeaderboard(userId, treeBenefits.coins);
    
    res.status(201).json({ 
      success: true,
      virtualCity: user.virtualCity
    });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

function calculateTreeBenefits(treeType) {
  // Simplified - would use actual environmental data
  const benefits = {
    'oak': { airQuality: 5, biodiversity: 8, coins: 50 },
    'maple': { airQuality: 4, biodiversity: 6, coins: 40 },
    'pine': { airQuality: 6, biodiversity: 5, coins: 45 }
  };
  return benefits[treeType] || { airQuality: 3, biodiversity: 4, coins: 30 };
}