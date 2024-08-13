import React, { useState } from 'react';

const CpfValidator = () => {
  const [cpf, setCpf] = useState('');
  const [response, setResponse] = useState(null);

  const handleSubmit = async (event) => {
    event.preventDefault();

    const data = { cpf };

    try {
      const res = await fetch('http://localhost:8000/checkers/brada', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`
        },
        body: JSON.stringify(data),

      }, 150000);

      if (!res.ok) {
        throw new Error('Erro ao enviar o CPF');
      }

      const json = await res.json();
      setResponse(json);
    } catch (error) {
      console.error('Erro:', error);
      setResponse({ error: 'Falha ao conectar com a API' });
    }
  };

  const renderTableFromData = (data) => {
    if (!data) return null;

    const { Saldos, card } = data; // Desestruturando os dados
    const saldoEntries = Saldos ? Object.entries(Saldos) : [];

    return (
      <div style={{ maxWidth: '600px', margin: '20px auto' }}>
        {card && (
          <table style={{ borderCollapse: 'collapse', width: '100%', marginBottom: '20px' }}>
            <tbody>
              <tr>
                <td style={{ borderBottom: '1px solid white', padding: '10px', textAlign: 'left' }}>
                  <strong>Card:</strong>
                </td>
                <td style={{ borderBottom: '1px solid white', padding: '10px', textAlign: 'left' }}>
                  {card}
                </td>
              </tr>
            </tbody>
          </table>
        )}
        {saldoEntries.length > 0 && (
          <table style={{ borderCollapse: 'collapse', width: '100%' }}>
            <thead>
              <tr>
                <th style={{ borderBottom: '1px solid white', padding: '10px', textAlign: 'left' }}>Descrição</th>
                <th style={{ borderBottom: '1px solid white', padding: '10px', textAlign: 'left' }}>Valor</th>
              </tr>
            </thead>
            <tbody>
              {saldoEntries.map(([key, value]) => (
                <tr key={key}>
                  <td style={{ borderBottom: '1px solid white', padding: '10px', textAlign: 'left' }}>
                    {key.replace(/([A-Z])/g, ' $1').replace(/^./, str => str.toUpperCase())} {/* Formatação opcional */}
                  </td>
                  <td style={{ borderBottom: '1px solid white', padding: '10px', textAlign: 'left' }}>
                    {value}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    );
  };

  return (
    <div style={{
        backgroundColor: 'black',
        color: 'white',
        minHeight: '100vh',
        padding: '20px',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center'
      }}>
        <h1>Consulta Saldo Bradesco</h1>
        <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
          <input
            type="text"
            value={cpf}
            onChange={(e) => setCpf(e.target.value)}
            placeholder="Digite o CPF"
            style={{ padding: '10px', fontSize: '16px', width: '300px', textAlign: 'center' }}
          />
          <button type="submit" style={{ marginTop: '10px', padding: '10px 20px', fontSize: '16px' }}>
            Enviar
          </button>
        </form>
        {response && (
          <div style={{ marginTop: '20px', textAlign: 'center' }}>
            <h2>Resposta da API:</h2>
            {renderTableFromData(response.Data)}
          </div>
        )}
      </div>
  );
};

export default CpfValidator;
