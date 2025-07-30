
import 'package:flutter/material.dart';
import '../../../core/components/navbar.dart';
import '../../../core/components/footer.dart';

class ContactPage extends StatefulWidget {
  @override
  _ContactPageState createState() => _ContactPageState();
}

class _ContactPageState extends State<ContactPage> {
  final _formKey = GlobalKey<FormState>();
  final _nombreController = TextEditingController();
  final _correoController = TextEditingController();
  final _consultaController = TextEditingController();
  String _tipoUsuario = 'Productor';
  String _region = 'Maule';
  bool enviado = false;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: Navbar(),
      body: Padding(
        padding: EdgeInsets.all(24),
        child: Form(
          key: _formKey,
          child: ListView(
            children: [
              Text("Contacto / Cotización", style: TextStyle(fontSize: 28, fontWeight: FontWeight.bold)),
              SizedBox(height: 16),
              Text("Solicita una cotización o contáctanos directamente"),
              SizedBox(height: 16),
              TextFormField(
                controller: _nombreController,
                decoration: InputDecoration(labelText: 'Nombre'),
                validator: (value) => value == null || value.isEmpty ? 'Campo obligatorio' : null,
              ),
              TextFormField(
                controller: _correoController,
                decoration: InputDecoration(labelText: 'Correo'),
                validator: (value) => value == null || !value.contains('@') ? 'Correo inválido' : null,
              ),
              DropdownButtonFormField<String>(
                value: _tipoUsuario,
                decoration: InputDecoration(labelText: 'Tipo de usuario'),
                items: ['Productor', 'Asesor Técnico', 'Inversionista', 'Investigador']
                  .map((e) => DropdownMenuItem(value: e, child: Text(e))).toList(),
                onChanged: (val) => setState(() => _tipoUsuario = val!),
              ),
              DropdownButtonFormField<String>(
                value: _region,
                decoration: InputDecoration(labelText: 'Región'),
                items: ['Maule', 'O’Higgins', 'Ñuble', 'Biobío']
                  .map((e) => DropdownMenuItem(value: e, child: Text(e))).toList(),
                onChanged: (val) => setState(() => _region = val!),
              ),
              TextFormField(
                controller: _consultaController,
                decoration: InputDecoration(labelText: 'Consulta'),
                maxLines: 4,
                validator: (value) => value == null || value.isEmpty ? 'Campo obligatorio' : null,
              ),
              SizedBox(height: 24),
              ElevatedButton(
                onPressed: () {
                  if (_formKey.currentState!.validate()) {
                    setState(() => enviado = true);
                  }
                },
                child: Text("Solicitar Cotización"),
              ),
              if (enviado)
                Padding(
                  padding: const EdgeInsets.only(top: 16.0),
                  child: Text(
                    "Mensaje enviado correctamente.",
                    style: TextStyle(color: Colors.green, fontWeight: FontWeight.bold),
                  ),
                )
            ],
          ),
        ),
      ),
      bottomNavigationBar: Footer(),
    );
  }
}
