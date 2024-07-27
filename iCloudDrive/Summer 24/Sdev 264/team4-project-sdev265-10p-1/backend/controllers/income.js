const { body, validationResult } = require('express-validator')
const IncomeSchema = require("../models/IncomeModel")

//just like in the expense.js 

exports.addIncome = [
    body('title')
      .notEmpty().withMessage('Title is required')
      .isLength({ max: 50 }).withMessage('Title must be less than 50 characters')
      .escape().trim(),
    body('amount')
      .isFloat({ gt: 0 }).withMessage('Amount must be a positive number'),
    body('category')
      .notEmpty().withMessage('Category is required')
      .isLength({ max: 50 }).withMessage('Category must be less than 50 characters')
      .escape().trim(),
    body('description')
      .notEmpty().withMessage('Description is required')
      .isLength({ max: 200 }).withMessage('Description must be less than 200 characters')
      .escape().trim(),
    body('date')
      .notEmpty().withMessage('Date is required')
      .isISO8601().withMessage('Date must be a valid date')
      .toDate(),
  
    async (req, res) => {
      const errors = validationResult(req);
      if (!errors.isEmpty()) {
        return res.status(400).json({ errors: errors.array() });
      }
  
      const { title, amount, category, description, date } = req.body;
  
      const income = new IncomeSchema({
        title,
        amount,
        category,
        description,
        date
      });
  
      try {
        await income.save();
        res.status(200).json({ message: 'Income Added' });
      } catch (error) {
        res.status(500).json({ message: 'Server Error' });
      }
  
      console.log(income);
    }
  ];
// exports.addIncome = async (req, res) => {
//     const {title, amount, category, description, date} = req.body

//     const income = IncomeSchema({
//         title, 
//         amount, 
//         category,
//         description,
//         date
//     })

//     try {
//         //validations
//         if(!title || !category || !description || !date){
//             return res.status(400).json({message: 'All fields are required'})
//         }
//         if(amount <=0 || !amount === 'number' ){
//             return res.status(400).json({message: 'Amount must be a positive number'})
//         }
//         await income.save()
//         res.status(200).json({message: 'Income Added'})
//     } catch (error) {
//         res.status(500).json({message: 'Server Error'})
        
//     }
//     console.log(income)
// }

exports.getIncomes = async (req, res) => {
    try {
        const incomes = await IncomeSchema.find().sort({createdAt: -1})
        res.status(200).json(incomes)
    } catch (error) {
        res.status(500).json({message: 'Server Error'})
    }
}
// I updated the function to add error messeage in case it cant find any income
exports.deleteIncome = async (req, res) => {
    const { id } = req.params;
    try {
      const income = await IncomeSchema.findByIdAndDelete(id);
      if (!income) {
        return res.status(404).json({ message: 'Income not found' });
      }
      res.status(200).json({ message: 'Income Deleted' });
    } catch (err) {
      res.status(500).json({ message: 'Server Error' });
    }
  };

// exports.deleteIncome = async (req, res) => {
//     const {id} = req.params;
//     IncomeSchema.findByIdAndDelete(id)
//         .then((income) => {
//             res.status(200).json({message: 'Income Deleted'})
//         })
//         .catch ((err) =>{
//             res.status(500).json({message: 'Server Error'})
//         })
// }