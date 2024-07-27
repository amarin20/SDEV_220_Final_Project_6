const mongoose = require('mongoose');


const ExpenseSchema = new mongoose.Schema({
    title: {
        type: String,
        required: true,
        trim: true,
        maxLength: 50
    },
    amount: {
        type: Number,
        required: true,
        min:0, //amount cannot be negative
        maxLength: 20,
        trim: true
    },
    type: {
        type: String,
        default: "expense"
    },
    date: {
        type: Date,
        required: true,
        trim: true
    },
    category: {
        type: String,
        required: true,
        maxLength:50, //keeps consistency 
        trim: true
    },
    description: {
        type: String,
        required: true,
        maxLength: 200, //Increased maxLength for more detailed descriptions
        trim: true
    },
}, {timestamps: true})



// Pre-save hook to sanitize inputs
ExpenseSchema.pre('save', function(next) {
    // Sanitize the title, category, and description fields by removing $ and . characters
    // This helps prevent NoSQL injection attacks
    this.title = this.title.replace(/[$.]/g, '');
    this.category = this.category.replace(/[$.]/g, '');
    this.description = this.description.replace(/[$.]/g, '');
    next(); 
});


module.exports = mongoose.model('Expense', ExpenseSchema)