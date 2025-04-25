// backend/models/User.js
const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
  username: { type: String, required: true, unique: true },
  email: { type: String, required: true, unique: true },
  password: { type: String, required: true },
  virtualCity: {
    treesPlanted: { type: Number, default: 0 },
    airQuality: { type: Number, default: 50 },
    biodiversity: { type: Number, default: 50 },
    coins: { type: Number, default: 0 },
    unlockedFeatures: { type: [String], default: [] }
  },
  leaderboardStats: {
    totalTrees: { type: Number, default: 0 },
    lastPlanted: { type: Date },
    rank: { type: Number }
  }
});

module.exports = mongoose.model('User', userSchema);