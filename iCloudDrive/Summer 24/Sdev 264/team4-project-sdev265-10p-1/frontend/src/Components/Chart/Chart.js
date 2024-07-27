import React from "react";
import {
    Chart as ChartJs, 
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend,
    ArcElement,
} from 'chart.js'

import {Line} from 'react-chartjs-2'
import styled from "styled-components";
import { useGlobalContext } from "../../context/globalContext";
import { dateFormat } from "../../utils/dateFormat";

ChartJs.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend,
    ArcElement,
)

function Chart() {
    const {incomes, expenses} = useGlobalContext()

    if (incomes.length === 0 && expenses.length === 0) {
        return <p>Enter incomes and expenses to see data on chart</p>
    }

    // Sort incomes and expenses by date
    const sortedIncomes = [...incomes].sort((a, b) => new Date(a.date) - new Date(b.date));
    const sortedExpenses = [...expenses].sort((a, b) => new Date(a.date) - new Date(b.date));

    const data = {
        labels: sortedIncomes.map((inc) => dateFormat(inc.date)),
        datasets: [
            {
                label: 'Income',
                data: sortedIncomes.map((income) => income.amount),
                backgroundColor: 'rgba(0, 128, 0, 0.2)',
                borderColor: 'rgba(0, 128, 0, 1)',
                tension: 0.2,
            },
            {
                label: 'Expenses',
                data: sortedExpenses.map((expense) => expense.amount),
                backgroundColor: 'rgba(255, 0, 0, 0.2)',
                borderColor: 'rgba(255, 0, 0, 1)',
                tension: 0.2,
            },
        ],
    };

    const options = {
        scales: {
            y: {
                ticks: {
                    callback: function(value) {
                        return '$' + value;
                    }
                }
            }
        }
    };

    return (
        <ChartStyled>
            <Line data={data} options={options} />
        </ChartStyled>
    );
}
const ChartStyled = styled.div`
    background: #fcf6f9;
    border: 2px solid #FFFFFF;
    box-shadow: 0px 1px 15px rgba(0, 0, 0, 0.6);
    padding: 1rem;
    border-radius: 20px;
    height: 100%
`;

export default Chart