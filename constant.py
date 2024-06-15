import pandas as pd

edu = [['B.Tech', 'M.E.', '2011', 'G.I.T.A. Odhisa', '81%'],
       ['12th', 'Science', '2009', 'I.V.M. Odisha', '86%'],
       ['10th', '-', '2007', 'I.V.M. Odisha', '82%']]

info = {'name': 'Radharani Ray',
        'Brief': 'SAP ABAP Consultant with 10+ years of experience, looking to resolve complex business problems '
                  'using new age offerings from SAP, and harnessing the power of AI; '
                  'Love to learn new things. Right now: python, Machine Learning, Artificial Intelligence, Azure!!',
                  'photo': {'path': 'abc.jpg', 'width': 150},
        'Mobile': '+91-6361106846', 'Email': 'radharay026@gmail.com', 'City': 'Bangalore, Karnataka',
        'edu': pd.DataFrame(edu, columns=['Qualification', 'Stream', 'Year', 'Institute', 'Score']),
        'skills': ['SAP ABAP', 'ABAP on HANA', 'SAP iRPA', 'SAP CAI', 'SAP DataHub', 'SAP BAS', 'SAP APO',
                   'SAP GTS', 'SAP SD', 'IDoc', 'ABAP proxy', 'WebDynpro', 'Unit Testing', 'Analytics with CDS',
                   'Development Lead', 'Innovation Lead', 'Issue Management', 'Production Support'],
        'achievements': ['Client Excellence Award for delivering critical objects and performance tuning at IBM',
                         'Technical Wizard Award by British Petroleum']}

skill_col_size = 5
embed_component = {
    'linkedin': """<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
        <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="dark" data-type="VERTICAL" data-vanity="radha-ray-sap-innovation-lead-9415354a" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://se.linkedin.com/in/radha-ray-sap-innovation-lead-9415354a?trk=profile-badge">Radha Ray (SAP, Innovation Lead)</a></div>
              """,
                  }

typ_day = ['Leading Development cycle;\nInvolve in business requirements;\nDeveloping objects from FSD and designing TSD and UTP',
           'Innovation & Business value creation;\nPlanning & Decision making with client process optimization',
           'Simplified Business Process;\nBest practice implementation;\nOwn knowledge upgrade',
           'Learning & Development new technologies (Azure, AI)',
           'Project delivery methodology & planning;\nOn-shore, near-shore, off-shore co-ordination;\nHelping junior resources on tech']
