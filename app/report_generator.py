from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    HRFlowable,
    Table,
    TableStyle,
    PageBreak
)

from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle
)

from reportlab.lib.units import inch

from reportlab.lib import colors

from reportlab.lib.enums import TA_CENTER, TA_LEFT

from datetime import datetime


def generate_report(
    prediction,
    probability,
    risk_level,
    segment,
    revenue_loss,
    reasons,
    strategies,
    filename="report.pdf"
):

    doc = SimpleDocTemplate(
        filename,
        rightMargin=0.5*inch,
        leftMargin=0.5*inch,
        topMargin=0.75*inch,
        bottomMargin=0.75*inch
    )

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#1f4788'),
        spaceAfter=6,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )

    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=13,
        textColor=colors.HexColor('#ffffff'),
        backColor=colors.HexColor('#1f4788'),
        spaceAfter=8,
        padding=8,
        fontName='Helvetica-Bold',
        alignment=TA_CENTER
    )

    elements = []

    # Professional Header
    elements.append(Spacer(1, 12))
    elements.append(
        Paragraph(
            "CUSTOMER CHURN ANALYSIS REPORT",
            title_style
        )
    )
    elements.append(Spacer(1, 6))
    elements.append(HRFlowable(width="100%", thickness=3, color=colors.HexColor('#1f4788')))
    elements.append(Spacer(1, 18))

    # Prediction Summary Box
    prediction_score = round(probability*100, 2)
    pred_color = colors.HexColor('#d32f2f') if prediction == "Likely To Churn" else colors.HexColor('#388e3c')

    pred_data = [
        [
            Paragraph("<b>PREDICTION RESULT</b>", styles['Heading3']),
            Paragraph(prediction, heading_style)
        ],
        [
            Paragraph("<b>Risk Score:</b>", styles['Normal']),
            Paragraph(f"<font color='#d32f2f'><b>{prediction_score}%</b></font>", styles['Normal'])
        ],
        [
            Paragraph("<b>Risk Level:</b>", styles['Normal']),
            Paragraph(f"<b>{risk_level}</b>", styles['Normal'])
        ]
    ]

    pred_table = Table(pred_data, colWidths=[2.5*inch, 2.5*inch])
    pred_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (1, 0), colors.HexColor('#1f4788')),
        ('TEXTCOLOR', (0, 0), (1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (1, 0), 12),
        ('TOPPADDING', (0, 0), (1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f5f5f5')),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#cccccc')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f9f9f9')]),
        ('LEFTPADDING', (0, 0), (-1, -1), 12),
        ('RIGHTPADDING', (0, 0), (-1, -1), 12),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))

    elements.append(pred_table)
    elements.append(Spacer(1, 18))

    # Customer Segment & Business Impact Box
    info_data = [
        [
            Paragraph("<b>CUSTOMER SEGMENT</b>", styles['Heading3']),
            Paragraph("<b>BUSINESS IMPACT</b>", styles['Heading3'])
        ],
        [
            Paragraph(segment, styles['Normal']),
            Paragraph(f"${revenue_loss}", styles['Normal'])
        ]
    ]

    info_table = Table(info_data, colWidths=[2.5*inch, 2.5*inch])
    info_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (1, 0), colors.HexColor('#1f4788')),
        ('TEXTCOLOR', (0, 0), (1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (1, 0), 11),
        ('BOTTOMPADDING', (0, 0), (1, 0), 10),
        ('TOPPADDING', (0, 0), (1, 0), 10),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f5f5f5')),
        ('GRID', (0, 0), (-1, -1), 1.5, colors.HexColor('#1f4788')),
        ('LEFTPADDING', (0, 0), (-1, -1), 12),
        ('RIGHTPADDING', (0, 0), (-1, -1), 12),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('FONTSIZE', (0, 1), (-1, -1), 13),
    ]))

    elements.append(info_table)
    elements.append(Spacer(1, 18))

    # Churn Drivers Section
    elements.append(
        Paragraph(
            "TOP CHURN DRIVERS",
            styles['Heading2']
        )
    )
    elements.append(Spacer(1, 8))

    reasons_data = [[Paragraph(f"• {reason}", styles['Normal'])] for reason in reasons]
    reasons_table = Table(reasons_data, colWidths=[5*inch])
    reasons_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#fafafa')),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#e0e0e0')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 12),
        ('RIGHTPADDING', (0, 0), (-1, -1), 12),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('ROWBACKGROUNDS', (0, 0), (-1, -1), [colors.white, colors.HexColor('#f9f9f9')]),
    ]))

    elements.append(reasons_table)
    elements.append(Spacer(1, 18))

    # Recommended Actions Section
    elements.append(
        Paragraph(
            "RECOMMENDED ACTIONS",
            styles['Heading2']
        )
    )
    elements.append(Spacer(1, 8))

    strategies_data = [[Paragraph(f"• {strategy}", styles['Normal'])] for strategy in strategies]
    strategies_table = Table(strategies_data, colWidths=[5*inch])
    strategies_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#fafafa')),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#e0e0e0')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 12),
        ('RIGHTPADDING', (0, 0), (-1, -1), 12),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('ROWBACKGROUNDS', (0, 0), (-1, -1), [colors.white, colors.HexColor('#f9f9f9')]),
    ]))

    elements.append(strategies_table)
    elements.append(Spacer(1, 24))

    # Footer
    elements.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor('#1f4788')))
    elements.append(Spacer(1, 8))

    footer_style = ParagraphStyle(
        'Footer',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.HexColor('#666666'),
        alignment=TA_CENTER
    )

    elements.append(
        Paragraph(
            "AI-Powered Customer Churn Intelligence System",
            footer_style
        )
    )

    elements.append(
        Paragraph(
            f"Generated On: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}",
            footer_style
        )
    )

    elements.append(Spacer(1, 8))
    elements.append(
        Paragraph(
            "Confidential - For Internal Use Only",
            footer_style
        )
    )

    doc.build(elements)

    return filename