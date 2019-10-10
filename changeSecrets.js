const AWS = require('aws-sdk');

exports.handler = async (event) => {
    const secretName = 'sites';
    for (const secretName of apiList) {
        await Promise.all([
                changesecrets({ 
                    SecretId: `/preprod/${secretName}/v1`,
                    region: 'us-east-1'}),
                changesecrets({ 
                            SecretId: `/preprod/${secretName}/v1`,
                            region: 'eu-west-1'}),
                changesecrets({ 
                            SecretId: `/dev/${secretName}/v1`,
                            region: 'eu-west-1'})
            ]);
    }
    console.log('job is done');
    return;
};

const changesecrets =({ SecretId, region }) => {
        const sm = new AWS.SecretsManager({ region })
        return sm.getSecretValue({ SecretId }).promise()
            .then(({ SecretString }) => //replaceSecrets(SecretString))
            {
                const newSecret = replaceSecrets(SecretString);
                if (newSecret !== SecretString) return sm
                    .putSecretValue({ SecretId, SecretString: newSecret }).promise()
                    .then(()=>console.log(`${SecretId} in ${region} was changed`));
                // else console.log(`${SecretId} in ${region} is not needed to change`);
                return
            })
            // .then(SecretString => sm.putSecretValue({ SecretId, SecretString }).promise())
            .catch(ex => console.error(`${SecretId} in ${region} error ${ex}` ) );
    }

const replaceSecrets = (SecretString) =>  SecretString
            .replace('preprod1-us-dse.brb-labs.com', 'dse1-us.ps-preprod.brb.')
            .replace('preprod2-us-dse.brb-labs.com', 'dse2-us.ps-preprod.brb.')
            .replace('preprod3-us-dse.brb-labs.com', 'dse3-us.ps-preprod.brb.')
            .replace('preprod1-eu-dse.brb-labs.com', 'dse1-eu.ps-preprod.brb.')
            .replace('preprod2-eu-dse.brb-labs.com', 'dse2-eu.ps-preprod.brb.')
            .replace('preprod3-eu-dse.brb-labs.com', 'dse3-eu.ps-preprod.brb.')
            
            .replace('dev1-dse6.brb-labs.com', 'dse1.ps-dev.brb.')
            .replace('dev2-dse6.brb-labs.com', 'dse2.ps-dev.brb.')
            .replace('dev3-dse6.brb-labs.com', 'dse3.ps-dev.brb.')
      
            .replace('redis-api-dev-eu-west-1.brb-labs.com','redis-eu-west-1.ps-dev.brb.')
            .replace('redis-api-preprod-eu-west-1.brb-labs.com','redis-eu-west-1.ps-preprod.brb.')
            .replace('redis-api-preprod-us-east-1.brb-labs.com','redis-us-east-1.ps-preprod.brb.')
            ;

const apiList = [  'sites',
  'sites-integration',
  'customers',
  'carts',
  'gift-cards',
  'inventory-integration',
  'customer-transactions',
  'inventory',
  'orders',
  'favourites',
  'stingray-ldap-access',
  'address-lookup',
  'ecom',
  'receipts',
  'external-orders',
  'phone-verification',
  'abandoned-carts',
  'cast-iron',
  'apple-pay-merchant-validation',
  'email-verification',
  'leads',
  'fixedposapi',
 ]
    // await sm.listSecrets({MaxResults: 100 }).promise()
    //     .then(async ({ SecretList }) => {
    //         console.log('Size:' + SecretList.length);
    //         await Promise.all(SecretList.map(({ Name }) => Name)).then(console.log);
            
    //     }
    //     );