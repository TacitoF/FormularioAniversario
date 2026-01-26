export default async function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).json({ error: 'Apenas POST' });

  const { nome, presenca, acompanhantes } = req.body;
  
  const GOOGLE_SCRIPT_URL = 'SUA_URL_DO_APPS_SCRIPT_AQUI';

  try {
    const response = await fetch(GOOGLE_SCRIPT_URL, {
      method: 'POST',
      body: JSON.stringify({
        nome,
        presenca,
        acompanhantes,
        data: new Date().toLocaleString('pt-BR')
      })
    });

    return res.status(200).json({ status: 'success' });
  } catch (err) {
    return res.status(500).json({ error: err.message });
  }
}